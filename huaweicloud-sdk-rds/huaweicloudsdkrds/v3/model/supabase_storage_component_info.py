# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseStorageComponentInfo:

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
        'ak': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'type': 'type',
        'bucket_name': 'bucket_name',
        'ak': 'ak'
    }

    def __init__(self, enabled=None, type=None, bucket_name=None, ak=None):
        r"""SupabaseStorageComponentInfo

        The model defined in huaweicloud sdk

        :param enabled: 
        :type enabled: bool
        :param type: 
        :type type: str
        :param bucket_name: 
        :type bucket_name: str
        :param ak: 
        :type ak: str
        """
        
        

        self._enabled = None
        self._type = None
        self._bucket_name = None
        self._ak = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if type is not None:
            self.type = type
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if ak is not None:
            self.ak = ak

    @property
    def enabled(self):
        r"""Gets the enabled of this SupabaseStorageComponentInfo.

        :return: The enabled of this SupabaseStorageComponentInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this SupabaseStorageComponentInfo.

        :param enabled: The enabled of this SupabaseStorageComponentInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def type(self):
        r"""Gets the type of this SupabaseStorageComponentInfo.

        :return: The type of this SupabaseStorageComponentInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SupabaseStorageComponentInfo.

        :param type: The type of this SupabaseStorageComponentInfo.
        :type type: str
        """
        self._type = type

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SupabaseStorageComponentInfo.

        :return: The bucket_name of this SupabaseStorageComponentInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SupabaseStorageComponentInfo.

        :param bucket_name: The bucket_name of this SupabaseStorageComponentInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def ak(self):
        r"""Gets the ak of this SupabaseStorageComponentInfo.

        :return: The ak of this SupabaseStorageComponentInfo.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this SupabaseStorageComponentInfo.

        :param ak: The ak of this SupabaseStorageComponentInfo.
        :type ak: str
        """
        self._ak = ak

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
        if not isinstance(other, SupabaseStorageComponentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
