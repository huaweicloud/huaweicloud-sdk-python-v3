# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckUrlSourceListFileFormatReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_bucket': 'str',
        'list_file_key': 'str',
        'ak': 'str',
        'sk': 'str',
        'region': 'str'
    }

    attribute_map = {
        'obs_bucket': 'obs_bucket',
        'list_file_key': 'list_file_key',
        'ak': 'ak',
        'sk': 'sk',
        'region': 'region'
    }

    def __init__(self, obs_bucket=None, list_file_key=None, ak=None, sk=None, region=None):
        r"""CheckUrlSourceListFileFormatReq

        The model defined in huaweicloud sdk

        :param obs_bucket: 存放对象列表文件的OBS桶名。 请确保与目的端桶处于同一区域，否则将导致任务创建失败。
        :type obs_bucket: str
        :param list_file_key: 对象列表文件或URL列表文件对象名。
        :type list_file_key: str
        :param ak: 目的端桶的AK（最大长度100个字符）。
        :type ak: str
        :param sk: 目的端桶的SK（最大长度100个字符）。
        :type sk: str
        :param region: 桶所处的区域。
        :type region: str
        """
        
        

        self._obs_bucket = None
        self._list_file_key = None
        self._ak = None
        self._sk = None
        self._region = None
        self.discriminator = None

        self.obs_bucket = obs_bucket
        self.list_file_key = list_file_key
        self.ak = ak
        self.sk = sk
        self.region = region

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this CheckUrlSourceListFileFormatReq.

        存放对象列表文件的OBS桶名。 请确保与目的端桶处于同一区域，否则将导致任务创建失败。

        :return: The obs_bucket of this CheckUrlSourceListFileFormatReq.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this CheckUrlSourceListFileFormatReq.

        存放对象列表文件的OBS桶名。 请确保与目的端桶处于同一区域，否则将导致任务创建失败。

        :param obs_bucket: The obs_bucket of this CheckUrlSourceListFileFormatReq.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def list_file_key(self):
        r"""Gets the list_file_key of this CheckUrlSourceListFileFormatReq.

        对象列表文件或URL列表文件对象名。

        :return: The list_file_key of this CheckUrlSourceListFileFormatReq.
        :rtype: str
        """
        return self._list_file_key

    @list_file_key.setter
    def list_file_key(self, list_file_key):
        r"""Sets the list_file_key of this CheckUrlSourceListFileFormatReq.

        对象列表文件或URL列表文件对象名。

        :param list_file_key: The list_file_key of this CheckUrlSourceListFileFormatReq.
        :type list_file_key: str
        """
        self._list_file_key = list_file_key

    @property
    def ak(self):
        r"""Gets the ak of this CheckUrlSourceListFileFormatReq.

        目的端桶的AK（最大长度100个字符）。

        :return: The ak of this CheckUrlSourceListFileFormatReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this CheckUrlSourceListFileFormatReq.

        目的端桶的AK（最大长度100个字符）。

        :param ak: The ak of this CheckUrlSourceListFileFormatReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this CheckUrlSourceListFileFormatReq.

        目的端桶的SK（最大长度100个字符）。

        :return: The sk of this CheckUrlSourceListFileFormatReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this CheckUrlSourceListFileFormatReq.

        目的端桶的SK（最大长度100个字符）。

        :param sk: The sk of this CheckUrlSourceListFileFormatReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def region(self):
        r"""Gets the region of this CheckUrlSourceListFileFormatReq.

        桶所处的区域。

        :return: The region of this CheckUrlSourceListFileFormatReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CheckUrlSourceListFileFormatReq.

        桶所处的区域。

        :param region: The region of this CheckUrlSourceListFileFormatReq.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, CheckUrlSourceListFileFormatReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
