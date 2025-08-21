# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyFilterDefinitionV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_ids': 'list[str]',
        'resource_types': 'list[str]',
        'resource_ids': 'list[str]',
        'tag_key_logic': 'str',
        'tags': 'list[FilterTagDetail]',
        'exclude_tag_key_logic': 'str',
        'exclude_tags': 'list[FilterTagDetail]'
    }

    attribute_map = {
        'region_ids': 'region_ids',
        'resource_types': 'resource_types',
        'resource_ids': 'resource_ids',
        'tag_key_logic': 'tag_key_logic',
        'tags': 'tags',
        'exclude_tag_key_logic': 'exclude_tag_key_logic',
        'exclude_tags': 'exclude_tags'
    }

    def __init__(self, region_ids=None, resource_types=None, resource_ids=None, tag_key_logic=None, tags=None, exclude_tag_key_logic=None, exclude_tags=None):
        r"""PolicyFilterDefinitionV2

        The model defined in huaweicloud sdk

        :param region_ids: 区域ID列表
        :type region_ids: list[str]
        :param resource_types: 云服务列表
        :type resource_types: list[str]
        :param resource_ids: 资源ID列表
        :type resource_ids: list[str]
        :param tag_key_logic: 参数tags的取值逻辑，例如tags设置了a:a和b:b，当取值AND时，表示规则仅对同时绑定了a:a和b:b的资源生效；当取值为OR时，表示规则对任何绑定了a:a或b:b的资源生效。
        :type tag_key_logic: str
        :param tags: 生效标签列表
        :type tags: list[:class:`huaweicloudsdkconfig.v1.FilterTagDetail`]
        :param exclude_tag_key_logic: 参数exclude_tags的取值逻辑，例如exclude_tags设置了a:a和b:b，当取值AND时，表示规则仅对同时绑定了a:a和b:b的资源生效；当取值为OR时，表示规则对任何绑定了a:a或b:b的资源生效。
        :type exclude_tag_key_logic: str
        :param exclude_tags: 排除标签列表，排除标签列表比生效标签列表有更高的优先级
        :type exclude_tags: list[:class:`huaweicloudsdkconfig.v1.FilterTagDetail`]
        """
        
        

        self._region_ids = None
        self._resource_types = None
        self._resource_ids = None
        self._tag_key_logic = None
        self._tags = None
        self._exclude_tag_key_logic = None
        self._exclude_tags = None
        self.discriminator = None

        if region_ids is not None:
            self.region_ids = region_ids
        if resource_types is not None:
            self.resource_types = resource_types
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if tag_key_logic is not None:
            self.tag_key_logic = tag_key_logic
        if tags is not None:
            self.tags = tags
        if exclude_tag_key_logic is not None:
            self.exclude_tag_key_logic = exclude_tag_key_logic
        if exclude_tags is not None:
            self.exclude_tags = exclude_tags

    @property
    def region_ids(self):
        r"""Gets the region_ids of this PolicyFilterDefinitionV2.

        区域ID列表

        :return: The region_ids of this PolicyFilterDefinitionV2.
        :rtype: list[str]
        """
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        r"""Sets the region_ids of this PolicyFilterDefinitionV2.

        区域ID列表

        :param region_ids: The region_ids of this PolicyFilterDefinitionV2.
        :type region_ids: list[str]
        """
        self._region_ids = region_ids

    @property
    def resource_types(self):
        r"""Gets the resource_types of this PolicyFilterDefinitionV2.

        云服务列表

        :return: The resource_types of this PolicyFilterDefinitionV2.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this PolicyFilterDefinitionV2.

        云服务列表

        :param resource_types: The resource_types of this PolicyFilterDefinitionV2.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this PolicyFilterDefinitionV2.

        资源ID列表

        :return: The resource_ids of this PolicyFilterDefinitionV2.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this PolicyFilterDefinitionV2.

        资源ID列表

        :param resource_ids: The resource_ids of this PolicyFilterDefinitionV2.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def tag_key_logic(self):
        r"""Gets the tag_key_logic of this PolicyFilterDefinitionV2.

        参数tags的取值逻辑，例如tags设置了a:a和b:b，当取值AND时，表示规则仅对同时绑定了a:a和b:b的资源生效；当取值为OR时，表示规则对任何绑定了a:a或b:b的资源生效。

        :return: The tag_key_logic of this PolicyFilterDefinitionV2.
        :rtype: str
        """
        return self._tag_key_logic

    @tag_key_logic.setter
    def tag_key_logic(self, tag_key_logic):
        r"""Sets the tag_key_logic of this PolicyFilterDefinitionV2.

        参数tags的取值逻辑，例如tags设置了a:a和b:b，当取值AND时，表示规则仅对同时绑定了a:a和b:b的资源生效；当取值为OR时，表示规则对任何绑定了a:a或b:b的资源生效。

        :param tag_key_logic: The tag_key_logic of this PolicyFilterDefinitionV2.
        :type tag_key_logic: str
        """
        self._tag_key_logic = tag_key_logic

    @property
    def tags(self):
        r"""Gets the tags of this PolicyFilterDefinitionV2.

        生效标签列表

        :return: The tags of this PolicyFilterDefinitionV2.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.FilterTagDetail`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PolicyFilterDefinitionV2.

        生效标签列表

        :param tags: The tags of this PolicyFilterDefinitionV2.
        :type tags: list[:class:`huaweicloudsdkconfig.v1.FilterTagDetail`]
        """
        self._tags = tags

    @property
    def exclude_tag_key_logic(self):
        r"""Gets the exclude_tag_key_logic of this PolicyFilterDefinitionV2.

        参数exclude_tags的取值逻辑，例如exclude_tags设置了a:a和b:b，当取值AND时，表示规则仅对同时绑定了a:a和b:b的资源生效；当取值为OR时，表示规则对任何绑定了a:a或b:b的资源生效。

        :return: The exclude_tag_key_logic of this PolicyFilterDefinitionV2.
        :rtype: str
        """
        return self._exclude_tag_key_logic

    @exclude_tag_key_logic.setter
    def exclude_tag_key_logic(self, exclude_tag_key_logic):
        r"""Sets the exclude_tag_key_logic of this PolicyFilterDefinitionV2.

        参数exclude_tags的取值逻辑，例如exclude_tags设置了a:a和b:b，当取值AND时，表示规则仅对同时绑定了a:a和b:b的资源生效；当取值为OR时，表示规则对任何绑定了a:a或b:b的资源生效。

        :param exclude_tag_key_logic: The exclude_tag_key_logic of this PolicyFilterDefinitionV2.
        :type exclude_tag_key_logic: str
        """
        self._exclude_tag_key_logic = exclude_tag_key_logic

    @property
    def exclude_tags(self):
        r"""Gets the exclude_tags of this PolicyFilterDefinitionV2.

        排除标签列表，排除标签列表比生效标签列表有更高的优先级

        :return: The exclude_tags of this PolicyFilterDefinitionV2.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.FilterTagDetail`]
        """
        return self._exclude_tags

    @exclude_tags.setter
    def exclude_tags(self, exclude_tags):
        r"""Sets the exclude_tags of this PolicyFilterDefinitionV2.

        排除标签列表，排除标签列表比生效标签列表有更高的优先级

        :param exclude_tags: The exclude_tags of this PolicyFilterDefinitionV2.
        :type exclude_tags: list[:class:`huaweicloudsdkconfig.v1.FilterTagDetail`]
        """
        self._exclude_tags = exclude_tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyFilterDefinitionV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
