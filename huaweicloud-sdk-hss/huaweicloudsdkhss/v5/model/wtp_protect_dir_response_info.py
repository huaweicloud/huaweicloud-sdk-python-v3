# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WtpProtectDirResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_dir_list': 'list[WtpProtectHostDirResponseInfo]',
        'exclue_file_type': 'str',
        'exclude_file_type': 'str',
        'protect_mode': 'str'
    }

    attribute_map = {
        'protect_dir_list': 'protect_dir_list',
        'exclue_file_type': 'exclue_file_type',
        'exclude_file_type': 'exclude_file_type',
        'protect_mode': 'protect_mode'
    }

    def __init__(self, protect_dir_list=None, exclue_file_type=None, exclude_file_type=None, protect_mode=None):
        r"""WtpProtectDirResponseInfo

        The model defined in huaweicloud sdk

        :param protect_dir_list: **参数解释**: 防护目录列表 **取值范围**: 最少0条，最多50条 
        :type protect_dir_list: list[:class:`huaweicloudsdkhss.v5.WtpProtectHostDirResponseInfo`]
        :param exclue_file_type: 排除文件类型
        :type exclue_file_type: str
        :param exclude_file_type: **参数解释**: 排除文件类型 **取值范围**: 字符长度0-512位 
        :type exclude_file_type: str
        :param protect_mode: **参数解释**: 防护模式 **取值范围**: - recovery ：拦截模式。 - alarm ：告警模式。 
        :type protect_mode: str
        """
        
        

        self._protect_dir_list = None
        self._exclue_file_type = None
        self._exclude_file_type = None
        self._protect_mode = None
        self.discriminator = None

        if protect_dir_list is not None:
            self.protect_dir_list = protect_dir_list
        if exclue_file_type is not None:
            self.exclue_file_type = exclue_file_type
        if exclude_file_type is not None:
            self.exclude_file_type = exclude_file_type
        if protect_mode is not None:
            self.protect_mode = protect_mode

    @property
    def protect_dir_list(self):
        r"""Gets the protect_dir_list of this WtpProtectDirResponseInfo.

        **参数解释**: 防护目录列表 **取值范围**: 最少0条，最多50条 

        :return: The protect_dir_list of this WtpProtectDirResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WtpProtectHostDirResponseInfo`]
        """
        return self._protect_dir_list

    @protect_dir_list.setter
    def protect_dir_list(self, protect_dir_list):
        r"""Sets the protect_dir_list of this WtpProtectDirResponseInfo.

        **参数解释**: 防护目录列表 **取值范围**: 最少0条，最多50条 

        :param protect_dir_list: The protect_dir_list of this WtpProtectDirResponseInfo.
        :type protect_dir_list: list[:class:`huaweicloudsdkhss.v5.WtpProtectHostDirResponseInfo`]
        """
        self._protect_dir_list = protect_dir_list

    @property
    def exclue_file_type(self):
        r"""Gets the exclue_file_type of this WtpProtectDirResponseInfo.

        排除文件类型

        :return: The exclue_file_type of this WtpProtectDirResponseInfo.
        :rtype: str
        """
        return self._exclue_file_type

    @exclue_file_type.setter
    def exclue_file_type(self, exclue_file_type):
        r"""Sets the exclue_file_type of this WtpProtectDirResponseInfo.

        排除文件类型

        :param exclue_file_type: The exclue_file_type of this WtpProtectDirResponseInfo.
        :type exclue_file_type: str
        """
        self._exclue_file_type = exclue_file_type

    @property
    def exclude_file_type(self):
        r"""Gets the exclude_file_type of this WtpProtectDirResponseInfo.

        **参数解释**: 排除文件类型 **取值范围**: 字符长度0-512位 

        :return: The exclude_file_type of this WtpProtectDirResponseInfo.
        :rtype: str
        """
        return self._exclude_file_type

    @exclude_file_type.setter
    def exclude_file_type(self, exclude_file_type):
        r"""Sets the exclude_file_type of this WtpProtectDirResponseInfo.

        **参数解释**: 排除文件类型 **取值范围**: 字符长度0-512位 

        :param exclude_file_type: The exclude_file_type of this WtpProtectDirResponseInfo.
        :type exclude_file_type: str
        """
        self._exclude_file_type = exclude_file_type

    @property
    def protect_mode(self):
        r"""Gets the protect_mode of this WtpProtectDirResponseInfo.

        **参数解释**: 防护模式 **取值范围**: - recovery ：拦截模式。 - alarm ：告警模式。 

        :return: The protect_mode of this WtpProtectDirResponseInfo.
        :rtype: str
        """
        return self._protect_mode

    @protect_mode.setter
    def protect_mode(self, protect_mode):
        r"""Sets the protect_mode of this WtpProtectDirResponseInfo.

        **参数解释**: 防护模式 **取值范围**: - recovery ：拦截模式。 - alarm ：告警模式。 

        :param protect_mode: The protect_mode of this WtpProtectDirResponseInfo.
        :type protect_mode: str
        """
        self._protect_mode = protect_mode

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
        if not isinstance(other, WtpProtectDirResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
