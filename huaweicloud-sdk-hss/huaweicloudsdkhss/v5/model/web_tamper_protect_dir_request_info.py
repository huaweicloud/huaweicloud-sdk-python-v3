# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperProtectDirRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_dir_list': 'list[WebTamperProtectHostDirRequestInfo]',
        'exclude_file_type': 'str',
        'exclue_file_type': 'str',
        'protect_mode': 'str'
    }

    attribute_map = {
        'protect_dir_list': 'protect_dir_list',
        'exclude_file_type': 'exclude_file_type',
        'exclue_file_type': 'exclue_file_type',
        'protect_mode': 'protect_mode'
    }

    def __init__(self, protect_dir_list=None, exclude_file_type=None, exclue_file_type=None, protect_mode=None):
        r"""WebTamperProtectDirRequestInfo

        The model defined in huaweicloud sdk

        :param protect_dir_list: 防护目录列表
        :type protect_dir_list: list[:class:`huaweicloudsdkhss.v5.WebTamperProtectHostDirRequestInfo`]
        :param exclude_file_type: 排除文件类型
        :type exclude_file_type: str
        :param exclue_file_type: 排除文件类型
        :type exclue_file_type: str
        :param protect_mode: **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - recovery ：拦截模式。 - alarm ：告警模式。  **默认取值**: recovery 
        :type protect_mode: str
        """
        
        

        self._protect_dir_list = None
        self._exclude_file_type = None
        self._exclue_file_type = None
        self._protect_mode = None
        self.discriminator = None

        if protect_dir_list is not None:
            self.protect_dir_list = protect_dir_list
        if exclude_file_type is not None:
            self.exclude_file_type = exclude_file_type
        if exclue_file_type is not None:
            self.exclue_file_type = exclue_file_type
        if protect_mode is not None:
            self.protect_mode = protect_mode

    @property
    def protect_dir_list(self):
        r"""Gets the protect_dir_list of this WebTamperProtectDirRequestInfo.

        防护目录列表

        :return: The protect_dir_list of this WebTamperProtectDirRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WebTamperProtectHostDirRequestInfo`]
        """
        return self._protect_dir_list

    @protect_dir_list.setter
    def protect_dir_list(self, protect_dir_list):
        r"""Sets the protect_dir_list of this WebTamperProtectDirRequestInfo.

        防护目录列表

        :param protect_dir_list: The protect_dir_list of this WebTamperProtectDirRequestInfo.
        :type protect_dir_list: list[:class:`huaweicloudsdkhss.v5.WebTamperProtectHostDirRequestInfo`]
        """
        self._protect_dir_list = protect_dir_list

    @property
    def exclude_file_type(self):
        r"""Gets the exclude_file_type of this WebTamperProtectDirRequestInfo.

        排除文件类型

        :return: The exclude_file_type of this WebTamperProtectDirRequestInfo.
        :rtype: str
        """
        return self._exclude_file_type

    @exclude_file_type.setter
    def exclude_file_type(self, exclude_file_type):
        r"""Sets the exclude_file_type of this WebTamperProtectDirRequestInfo.

        排除文件类型

        :param exclude_file_type: The exclude_file_type of this WebTamperProtectDirRequestInfo.
        :type exclude_file_type: str
        """
        self._exclude_file_type = exclude_file_type

    @property
    def exclue_file_type(self):
        r"""Gets the exclue_file_type of this WebTamperProtectDirRequestInfo.

        排除文件类型

        :return: The exclue_file_type of this WebTamperProtectDirRequestInfo.
        :rtype: str
        """
        return self._exclue_file_type

    @exclue_file_type.setter
    def exclue_file_type(self, exclue_file_type):
        r"""Sets the exclue_file_type of this WebTamperProtectDirRequestInfo.

        排除文件类型

        :param exclue_file_type: The exclue_file_type of this WebTamperProtectDirRequestInfo.
        :type exclue_file_type: str
        """
        self._exclue_file_type = exclue_file_type

    @property
    def protect_mode(self):
        r"""Gets the protect_mode of this WebTamperProtectDirRequestInfo.

        **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - recovery ：拦截模式。 - alarm ：告警模式。  **默认取值**: recovery 

        :return: The protect_mode of this WebTamperProtectDirRequestInfo.
        :rtype: str
        """
        return self._protect_mode

    @protect_mode.setter
    def protect_mode(self, protect_mode):
        r"""Sets the protect_mode of this WebTamperProtectDirRequestInfo.

        **参数解释**: 防护模式 **约束限制**: 不涉及 **取值范围**: - recovery ：拦截模式。 - alarm ：告警模式。  **默认取值**: recovery 

        :param protect_mode: The protect_mode of this WebTamperProtectDirRequestInfo.
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
        if not isinstance(other, WebTamperProtectDirRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
