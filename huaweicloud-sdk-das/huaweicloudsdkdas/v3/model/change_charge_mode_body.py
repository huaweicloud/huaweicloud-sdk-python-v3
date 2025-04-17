# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeChargeModeBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id_list': 'list[str]',
        'datastore_type': 'str'
    }

    attribute_map = {
        'instance_id_list': 'instance_id_list',
        'datastore_type': 'datastore_type'
    }

    def __init__(self, instance_id_list=None, datastore_type=None):
        r"""ChangeChargeModeBody

        The model defined in huaweicloud sdk

        :param instance_id_list: 实例ID列表
        :type instance_id_list: list[str]
        :param datastore_type: 引擎类型
        :type datastore_type: str
        """
        
        

        self._instance_id_list = None
        self._datastore_type = None
        self.discriminator = None

        self.instance_id_list = instance_id_list
        self.datastore_type = datastore_type

    @property
    def instance_id_list(self):
        r"""Gets the instance_id_list of this ChangeChargeModeBody.

        实例ID列表

        :return: The instance_id_list of this ChangeChargeModeBody.
        :rtype: list[str]
        """
        return self._instance_id_list

    @instance_id_list.setter
    def instance_id_list(self, instance_id_list):
        r"""Sets the instance_id_list of this ChangeChargeModeBody.

        实例ID列表

        :param instance_id_list: The instance_id_list of this ChangeChargeModeBody.
        :type instance_id_list: list[str]
        """
        self._instance_id_list = instance_id_list

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ChangeChargeModeBody.

        引擎类型

        :return: The datastore_type of this ChangeChargeModeBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ChangeChargeModeBody.

        引擎类型

        :param datastore_type: The datastore_type of this ChangeChargeModeBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

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
        if not isinstance(other, ChangeChargeModeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
