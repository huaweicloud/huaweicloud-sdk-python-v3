# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateApplicationViewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_list': 'list[BatchCreateApplicationViewRequestBodyApplicationList]',
        'component_list': 'list[BatchCreateApplicationViewRequestBodyComponentList]',
        'group_list': 'list[BatchCreateApplicationViewRequestBodyGroupList]'
    }

    attribute_map = {
        'application_list': 'application_list',
        'component_list': 'component_list',
        'group_list': 'group_list'
    }

    def __init__(self, application_list=None, component_list=None, group_list=None):
        r"""BatchCreateApplicationViewRequestBody

        The model defined in huaweicloud sdk

        :param application_list: **参数解释：** 应用信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type application_list: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyApplicationList`]
        :param component_list: **参数解释：** 组件信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type component_list: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyComponentList`]
        :param group_list: **参数解释：** 分组信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type group_list: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyGroupList`]
        """
        
        

        self._application_list = None
        self._component_list = None
        self._group_list = None
        self.discriminator = None

        self.application_list = application_list
        if component_list is not None:
            self.component_list = component_list
        if group_list is not None:
            self.group_list = group_list

    @property
    def application_list(self):
        r"""Gets the application_list of this BatchCreateApplicationViewRequestBody.

        **参数解释：** 应用信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The application_list of this BatchCreateApplicationViewRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyApplicationList`]
        """
        return self._application_list

    @application_list.setter
    def application_list(self, application_list):
        r"""Sets the application_list of this BatchCreateApplicationViewRequestBody.

        **参数解释：** 应用信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param application_list: The application_list of this BatchCreateApplicationViewRequestBody.
        :type application_list: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyApplicationList`]
        """
        self._application_list = application_list

    @property
    def component_list(self):
        r"""Gets the component_list of this BatchCreateApplicationViewRequestBody.

        **参数解释：** 组件信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The component_list of this BatchCreateApplicationViewRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyComponentList`]
        """
        return self._component_list

    @component_list.setter
    def component_list(self, component_list):
        r"""Sets the component_list of this BatchCreateApplicationViewRequestBody.

        **参数解释：** 组件信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param component_list: The component_list of this BatchCreateApplicationViewRequestBody.
        :type component_list: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyComponentList`]
        """
        self._component_list = component_list

    @property
    def group_list(self):
        r"""Gets the group_list of this BatchCreateApplicationViewRequestBody.

        **参数解释：** 分组信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The group_list of this BatchCreateApplicationViewRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyGroupList`]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        r"""Sets the group_list of this BatchCreateApplicationViewRequestBody.

        **参数解释：** 分组信息组成的列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param group_list: The group_list of this BatchCreateApplicationViewRequestBody.
        :type group_list: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodyGroupList`]
        """
        self._group_list = group_list

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
        if not isinstance(other, BatchCreateApplicationViewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
