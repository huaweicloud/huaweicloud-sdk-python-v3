# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifySupabaseApplicationStorageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'type': 'str',
        'bucket_name': 'str',
        'ak': 'str',
        'sk': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'type': 'type',
        'bucket_name': 'bucket_name',
        'ak': 'ak',
        'sk': 'sk'
    }

    def __init__(self, enabled=None, type=None, bucket_name=None, ak=None, sk=None):
        r"""ModifySupabaseApplicationStorageRequestBody

        The model defined in huaweicloud sdk

        :param enabled: 
        :type enabled: bool
        :param type: 
        :type type: str
        :param bucket_name: 
        :type bucket_name: str
        :param ak: 
        :type ak: str
        :param sk: show不返回，部分更新省略即保留。
        :type sk: str
        """
        
        

        self._enabled = None
        self._type = None
        self._bucket_name = None
        self._ak = None
        self._sk = None
        self.discriminator = None

        self.enabled = enabled
        if type is not None:
            self.type = type
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk

    @property
    def enabled(self):
        r"""Gets the enabled of this ModifySupabaseApplicationStorageRequestBody.

        :return: The enabled of this ModifySupabaseApplicationStorageRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ModifySupabaseApplicationStorageRequestBody.

        :param enabled: The enabled of this ModifySupabaseApplicationStorageRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def type(self):
        r"""Gets the type of this ModifySupabaseApplicationStorageRequestBody.

        :return: The type of this ModifySupabaseApplicationStorageRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModifySupabaseApplicationStorageRequestBody.

        :param type: The type of this ModifySupabaseApplicationStorageRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ModifySupabaseApplicationStorageRequestBody.

        :return: The bucket_name of this ModifySupabaseApplicationStorageRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ModifySupabaseApplicationStorageRequestBody.

        :param bucket_name: The bucket_name of this ModifySupabaseApplicationStorageRequestBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def ak(self):
        r"""Gets the ak of this ModifySupabaseApplicationStorageRequestBody.

        :return: The ak of this ModifySupabaseApplicationStorageRequestBody.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this ModifySupabaseApplicationStorageRequestBody.

        :param ak: The ak of this ModifySupabaseApplicationStorageRequestBody.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this ModifySupabaseApplicationStorageRequestBody.

        show不返回，部分更新省略即保留。

        :return: The sk of this ModifySupabaseApplicationStorageRequestBody.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this ModifySupabaseApplicationStorageRequestBody.

        show不返回，部分更新省略即保留。

        :param sk: The sk of this ModifySupabaseApplicationStorageRequestBody.
        :type sk: str
        """
        self._sk = sk

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifySupabaseApplicationStorageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
