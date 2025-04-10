# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchEipStatusDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'object_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'object_id': 'object_id',
        'status': 'status'
    }

    def __init__(self, fw_instance_id=None, object_id=None, status=None):
        r"""SwitchEipStatusDto

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙id
        :type fw_instance_id: str
        :param object_id: 防护对象id
        :type object_id: str
        :param status: 是否开启新增eip自动防护，1；是，0：否
        :type status: int
        """
        
        

        self._fw_instance_id = None
        self._object_id = None
        self._status = None
        self.discriminator = None

        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if object_id is not None:
            self.object_id = object_id
        if status is not None:
            self.status = status

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this SwitchEipStatusDto.

        防火墙id

        :return: The fw_instance_id of this SwitchEipStatusDto.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this SwitchEipStatusDto.

        防火墙id

        :param fw_instance_id: The fw_instance_id of this SwitchEipStatusDto.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def object_id(self):
        r"""Gets the object_id of this SwitchEipStatusDto.

        防护对象id

        :return: The object_id of this SwitchEipStatusDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this SwitchEipStatusDto.

        防护对象id

        :param object_id: The object_id of this SwitchEipStatusDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def status(self):
        r"""Gets the status of this SwitchEipStatusDto.

        是否开启新增eip自动防护，1；是，0：否

        :return: The status of this SwitchEipStatusDto.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SwitchEipStatusDto.

        是否开启新增eip自动防护，1；是，0：否

        :param status: The status of this SwitchEipStatusDto.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, SwitchEipStatusDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
