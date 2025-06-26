# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadKeystoreRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file',
        'privacy': 'str',
        'description': 'str'
    }

    attribute_map = {
        'file': 'file',
        'privacy': 'privacy',
        'description': 'description'
    }

    def __init__(self, file=None, privacy=None, description=None):
        r"""UploadKeystoreRequestBody

        The model defined in huaweicloud sdk

        :param file: 文件
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param privacy: 同意隐私声明，允许使用用户敏感信息进行相关业务操作。
        :type privacy: str
        :param description: 文件描述
        :type description: str
        """
        
        

        self._file = None
        self._privacy = None
        self._description = None
        self.discriminator = None

        self.file = file
        self.privacy = privacy
        if description is not None:
            self.description = description

    @property
    def file(self):
        r"""Gets the file of this UploadKeystoreRequestBody.

        文件

        :return: The file of this UploadKeystoreRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this UploadKeystoreRequestBody.

        文件

        :param file: The file of this UploadKeystoreRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def privacy(self):
        r"""Gets the privacy of this UploadKeystoreRequestBody.

        同意隐私声明，允许使用用户敏感信息进行相关业务操作。

        :return: The privacy of this UploadKeystoreRequestBody.
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        r"""Sets the privacy of this UploadKeystoreRequestBody.

        同意隐私声明，允许使用用户敏感信息进行相关业务操作。

        :param privacy: The privacy of this UploadKeystoreRequestBody.
        :type privacy: str
        """
        self._privacy = privacy

    @property
    def description(self):
        r"""Gets the description of this UploadKeystoreRequestBody.

        文件描述

        :return: The description of this UploadKeystoreRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UploadKeystoreRequestBody.

        文件描述

        :param description: The description of this UploadKeystoreRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UploadKeystoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
