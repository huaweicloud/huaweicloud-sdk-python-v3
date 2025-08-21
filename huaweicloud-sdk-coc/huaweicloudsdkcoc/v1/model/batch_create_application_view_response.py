# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateApplicationViewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_ids': 'list[str]',
        'component_ids': 'list[str]',
        'group_ids': 'list[str]'
    }

    attribute_map = {
        'application_ids': 'application_ids',
        'component_ids': 'component_ids',
        'group_ids': 'group_ids'
    }

    def __init__(self, application_ids=None, component_ids=None, group_ids=None):
        r"""BatchCreateApplicationViewResponse

        The model defined in huaweicloud sdk

        :param application_ids: **参数解释：** 应用id列表。 **取值范围：** 不涉及。
        :type application_ids: list[str]
        :param component_ids: **参数解释：** 组件id列表。 **取值范围：** 不涉及。
        :type component_ids: list[str]
        :param group_ids: **参数解释：** 分组id列表。 **取值范围：** 不涉及。
        :type group_ids: list[str]
        """
        
        super(BatchCreateApplicationViewResponse, self).__init__()

        self._application_ids = None
        self._component_ids = None
        self._group_ids = None
        self.discriminator = None

        if application_ids is not None:
            self.application_ids = application_ids
        if component_ids is not None:
            self.component_ids = component_ids
        if group_ids is not None:
            self.group_ids = group_ids

    @property
    def application_ids(self):
        r"""Gets the application_ids of this BatchCreateApplicationViewResponse.

        **参数解释：** 应用id列表。 **取值范围：** 不涉及。

        :return: The application_ids of this BatchCreateApplicationViewResponse.
        :rtype: list[str]
        """
        return self._application_ids

    @application_ids.setter
    def application_ids(self, application_ids):
        r"""Sets the application_ids of this BatchCreateApplicationViewResponse.

        **参数解释：** 应用id列表。 **取值范围：** 不涉及。

        :param application_ids: The application_ids of this BatchCreateApplicationViewResponse.
        :type application_ids: list[str]
        """
        self._application_ids = application_ids

    @property
    def component_ids(self):
        r"""Gets the component_ids of this BatchCreateApplicationViewResponse.

        **参数解释：** 组件id列表。 **取值范围：** 不涉及。

        :return: The component_ids of this BatchCreateApplicationViewResponse.
        :rtype: list[str]
        """
        return self._component_ids

    @component_ids.setter
    def component_ids(self, component_ids):
        r"""Sets the component_ids of this BatchCreateApplicationViewResponse.

        **参数解释：** 组件id列表。 **取值范围：** 不涉及。

        :param component_ids: The component_ids of this BatchCreateApplicationViewResponse.
        :type component_ids: list[str]
        """
        self._component_ids = component_ids

    @property
    def group_ids(self):
        r"""Gets the group_ids of this BatchCreateApplicationViewResponse.

        **参数解释：** 分组id列表。 **取值范围：** 不涉及。

        :return: The group_ids of this BatchCreateApplicationViewResponse.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        r"""Sets the group_ids of this BatchCreateApplicationViewResponse.

        **参数解释：** 分组id列表。 **取值范围：** 不涉及。

        :param group_ids: The group_ids of this BatchCreateApplicationViewResponse.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

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
        if not isinstance(other, BatchCreateApplicationViewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
