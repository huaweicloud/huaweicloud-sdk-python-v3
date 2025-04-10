# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiGroupCheck:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'roma_app_id': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'roma_app_id': 'roma_app_id'
    }

    def __init__(self, group_name=None, roma_app_id=None):
        r"""ApiGroupCheck

        The model defined in huaweicloud sdk

        :param group_name: 待校验的API分组名称
        :type group_name: str
        :param roma_app_id: 集成应用ID  暂不支持
        :type roma_app_id: str
        """
        
        

        self._group_name = None
        self._roma_app_id = None
        self.discriminator = None

        self.group_name = group_name
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ApiGroupCheck.

        待校验的API分组名称

        :return: The group_name of this ApiGroupCheck.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ApiGroupCheck.

        待校验的API分组名称

        :param group_name: The group_name of this ApiGroupCheck.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def roma_app_id(self):
        r"""Gets the roma_app_id of this ApiGroupCheck.

        集成应用ID  暂不支持

        :return: The roma_app_id of this ApiGroupCheck.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        r"""Sets the roma_app_id of this ApiGroupCheck.

        集成应用ID  暂不支持

        :param roma_app_id: The roma_app_id of this ApiGroupCheck.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

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
        if not isinstance(other, ApiGroupCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
