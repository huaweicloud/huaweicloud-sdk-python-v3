# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecAppTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'int',
        'file': 'file',
        'privacy_statement_url': 'str',
        'personal_info_share_url': 'str'
    }

    attribute_map = {
        'version': 'version',
        'file': 'file',
        'privacy_statement_url': 'privacy_statement_url',
        'personal_info_share_url': 'personal_info_share_url'
    }

    def __init__(self, version=None, file=None, privacy_statement_url=None, personal_info_share_url=None):
        r"""CreateSecAppTaskRequestBody

        The model defined in huaweicloud sdk

        :param version: 版本：0免费版，1专业版
        :type version: int
        :param file: 待扫描文件，后缀为.apk或.hap,专业版大小限制为2G，免费版大小限制为100M
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param privacy_statement_url: 隐私申明URL
        :type privacy_statement_url: str
        :param personal_info_share_url: 个人信息第三方共享目录URL
        :type personal_info_share_url: str
        """
        
        

        self._version = None
        self._file = None
        self._privacy_statement_url = None
        self._personal_info_share_url = None
        self.discriminator = None

        self.version = version
        self.file = file
        if privacy_statement_url is not None:
            self.privacy_statement_url = privacy_statement_url
        if personal_info_share_url is not None:
            self.personal_info_share_url = personal_info_share_url

    @property
    def version(self):
        r"""Gets the version of this CreateSecAppTaskRequestBody.

        版本：0免费版，1专业版

        :return: The version of this CreateSecAppTaskRequestBody.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateSecAppTaskRequestBody.

        版本：0免费版，1专业版

        :param version: The version of this CreateSecAppTaskRequestBody.
        :type version: int
        """
        self._version = version

    @property
    def file(self):
        r"""Gets the file of this CreateSecAppTaskRequestBody.

        待扫描文件，后缀为.apk或.hap,专业版大小限制为2G，免费版大小限制为100M

        :return: The file of this CreateSecAppTaskRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this CreateSecAppTaskRequestBody.

        待扫描文件，后缀为.apk或.hap,专业版大小限制为2G，免费版大小限制为100M

        :param file: The file of this CreateSecAppTaskRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def privacy_statement_url(self):
        r"""Gets the privacy_statement_url of this CreateSecAppTaskRequestBody.

        隐私申明URL

        :return: The privacy_statement_url of this CreateSecAppTaskRequestBody.
        :rtype: str
        """
        return self._privacy_statement_url

    @privacy_statement_url.setter
    def privacy_statement_url(self, privacy_statement_url):
        r"""Sets the privacy_statement_url of this CreateSecAppTaskRequestBody.

        隐私申明URL

        :param privacy_statement_url: The privacy_statement_url of this CreateSecAppTaskRequestBody.
        :type privacy_statement_url: str
        """
        self._privacy_statement_url = privacy_statement_url

    @property
    def personal_info_share_url(self):
        r"""Gets the personal_info_share_url of this CreateSecAppTaskRequestBody.

        个人信息第三方共享目录URL

        :return: The personal_info_share_url of this CreateSecAppTaskRequestBody.
        :rtype: str
        """
        return self._personal_info_share_url

    @personal_info_share_url.setter
    def personal_info_share_url(self, personal_info_share_url):
        r"""Sets the personal_info_share_url of this CreateSecAppTaskRequestBody.

        个人信息第三方共享目录URL

        :param personal_info_share_url: The personal_info_share_url of this CreateSecAppTaskRequestBody.
        :type personal_info_share_url: str
        """
        self._personal_info_share_url = personal_info_share_url

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
        if not isinstance(other, CreateSecAppTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
