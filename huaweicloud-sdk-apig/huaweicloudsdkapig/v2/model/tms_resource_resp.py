# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmsResourceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resouce_detail': 'str',
        'resource_name': 'str',
        'tags': 'list[TmsKeyValue]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resouce_detail': 'resouce_detail',
        'resource_name': 'resource_name',
        'tags': 'tags'
    }

    def __init__(self, resource_id=None, resouce_detail=None, resource_name=None, tags=None):
        r"""TmsResourceResp

        The model defined in huaweicloud sdk

        :param resource_id: 实例编号
        :type resource_id: str
        :param resouce_detail: 实例详细描述。暂不支持
        :type resouce_detail: str
        :param resource_name: 实例名称
        :type resource_name: str
        :param tags: 实例绑定的标签列表
        :type tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValue`]
        """
        
        

        self._resource_id = None
        self._resouce_detail = None
        self._resource_name = None
        self._tags = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resouce_detail is not None:
            self.resouce_detail = resouce_detail
        if resource_name is not None:
            self.resource_name = resource_name
        if tags is not None:
            self.tags = tags

    @property
    def resource_id(self):
        r"""Gets the resource_id of this TmsResourceResp.

        实例编号

        :return: The resource_id of this TmsResourceResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this TmsResourceResp.

        实例编号

        :param resource_id: The resource_id of this TmsResourceResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resouce_detail(self):
        r"""Gets the resouce_detail of this TmsResourceResp.

        实例详细描述。暂不支持

        :return: The resouce_detail of this TmsResourceResp.
        :rtype: str
        """
        return self._resouce_detail

    @resouce_detail.setter
    def resouce_detail(self, resouce_detail):
        r"""Sets the resouce_detail of this TmsResourceResp.

        实例详细描述。暂不支持

        :param resouce_detail: The resouce_detail of this TmsResourceResp.
        :type resouce_detail: str
        """
        self._resouce_detail = resouce_detail

    @property
    def resource_name(self):
        r"""Gets the resource_name of this TmsResourceResp.

        实例名称

        :return: The resource_name of this TmsResourceResp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this TmsResourceResp.

        实例名称

        :param resource_name: The resource_name of this TmsResourceResp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def tags(self):
        r"""Gets the tags of this TmsResourceResp.

        实例绑定的标签列表

        :return: The tags of this TmsResourceResp.
        :rtype: list[:class:`huaweicloudsdkapig.v2.TmsKeyValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TmsResourceResp.

        实例绑定的标签列表

        :param tags: The tags of this TmsResourceResp.
        :type tags: list[:class:`huaweicloudsdkapig.v2.TmsKeyValue`]
        """
        self._tags = tags

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
        if not isinstance(other, TmsResourceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
