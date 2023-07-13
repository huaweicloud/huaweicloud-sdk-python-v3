# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEncryptdatasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encryptdata_id': 'str',
        'ief_instance_id': 'str',
        'body': 'EncryptDataReq'
    }

    attribute_map = {
        'encryptdata_id': 'encryptdata_id',
        'ief_instance_id': 'ief-instance-id',
        'body': 'body'
    }

    def __init__(self, encryptdata_id=None, ief_instance_id=None, body=None):
        """UpdateEncryptdatasRequest

        The model defined in huaweicloud sdk

        :param encryptdata_id: 加密数据ID
        :type encryptdata_id: str
        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param body: Body of the UpdateEncryptdatasRequest
        :type body: :class:`huaweicloudsdkief.v1.EncryptDataReq`
        """
        
        

        self._encryptdata_id = None
        self._ief_instance_id = None
        self._body = None
        self.discriminator = None

        self.encryptdata_id = encryptdata_id
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if body is not None:
            self.body = body

    @property
    def encryptdata_id(self):
        """Gets the encryptdata_id of this UpdateEncryptdatasRequest.

        加密数据ID

        :return: The encryptdata_id of this UpdateEncryptdatasRequest.
        :rtype: str
        """
        return self._encryptdata_id

    @encryptdata_id.setter
    def encryptdata_id(self, encryptdata_id):
        """Sets the encryptdata_id of this UpdateEncryptdatasRequest.

        加密数据ID

        :param encryptdata_id: The encryptdata_id of this UpdateEncryptdatasRequest.
        :type encryptdata_id: str
        """
        self._encryptdata_id = encryptdata_id

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this UpdateEncryptdatasRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this UpdateEncryptdatasRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this UpdateEncryptdatasRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this UpdateEncryptdatasRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def body(self):
        """Gets the body of this UpdateEncryptdatasRequest.

        :return: The body of this UpdateEncryptdatasRequest.
        :rtype: :class:`huaweicloudsdkief.v1.EncryptDataReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateEncryptdatasRequest.

        :param body: The body of this UpdateEncryptdatasRequest.
        :type body: :class:`huaweicloudsdkief.v1.EncryptDataReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateEncryptdatasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
