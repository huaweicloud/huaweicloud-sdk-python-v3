# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAdditionalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_number': 'int',
        'additional_info': 'dict(str, str)'
    }

    attribute_map = {
        'item_number': 'item_number',
        'additional_info': 'additional_info'
    }

    def __init__(self, item_number=None, additional_info=None):
        r"""TaskAdditionalInfo

        The model defined in huaweicloud sdk

        :param item_number: 附加信息条数
        :type item_number: int
        :param additional_info: 附加信息
        :type additional_info: dict(str, str)
        """
        
        

        self._item_number = None
        self._additional_info = None
        self.discriminator = None

        self.item_number = item_number
        self.additional_info = additional_info

    @property
    def item_number(self):
        r"""Gets the item_number of this TaskAdditionalInfo.

        附加信息条数

        :return: The item_number of this TaskAdditionalInfo.
        :rtype: int
        """
        return self._item_number

    @item_number.setter
    def item_number(self, item_number):
        r"""Sets the item_number of this TaskAdditionalInfo.

        附加信息条数

        :param item_number: The item_number of this TaskAdditionalInfo.
        :type item_number: int
        """
        self._item_number = item_number

    @property
    def additional_info(self):
        r"""Gets the additional_info of this TaskAdditionalInfo.

        附加信息

        :return: The additional_info of this TaskAdditionalInfo.
        :rtype: dict(str, str)
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        r"""Sets the additional_info of this TaskAdditionalInfo.

        附加信息

        :param additional_info: The additional_info of this TaskAdditionalInfo.
        :type additional_info: dict(str, str)
        """
        self._additional_info = additional_info

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
        if not isinstance(other, TaskAdditionalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
