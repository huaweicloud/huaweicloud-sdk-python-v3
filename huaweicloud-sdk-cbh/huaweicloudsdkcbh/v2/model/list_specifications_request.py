# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecificationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'spec_code': 'str'
    }

    attribute_map = {
        'action': 'action',
        'spec_code': 'spec_code'
    }

    def __init__(self, action=None, spec_code=None):
        r"""ListSpecificationsRequest

        The model defined in huaweicloud sdk

        :param action: 查询云堡垒机规格当前动作。 - create：查询可创建云堡垒机规格信息 - update：查询可变更云堡垒机规格信息
        :type action: str
        :param spec_code: 云堡垒机规格信息，当action为update时此字段必填。
        :type spec_code: str
        """
        
        

        self._action = None
        self._spec_code = None
        self.discriminator = None

        self.action = action
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def action(self):
        r"""Gets the action of this ListSpecificationsRequest.

        查询云堡垒机规格当前动作。 - create：查询可创建云堡垒机规格信息 - update：查询可变更云堡垒机规格信息

        :return: The action of this ListSpecificationsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListSpecificationsRequest.

        查询云堡垒机规格当前动作。 - create：查询可创建云堡垒机规格信息 - update：查询可变更云堡垒机规格信息

        :param action: The action of this ListSpecificationsRequest.
        :type action: str
        """
        self._action = action

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ListSpecificationsRequest.

        云堡垒机规格信息，当action为update时此字段必填。

        :return: The spec_code of this ListSpecificationsRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ListSpecificationsRequest.

        云堡垒机规格信息，当action为update时此字段必填。

        :param spec_code: The spec_code of this ListSpecificationsRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, ListSpecificationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
