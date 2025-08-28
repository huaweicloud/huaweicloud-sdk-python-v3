# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IacRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id_list': 'list[str]',
        'file_name': 'str',
        'file_type': 'str',
        'risky': 'bool',
        'scan_type': 'str'
    }

    attribute_map = {
        'file_id_list': 'file_id_list',
        'file_name': 'file_name',
        'file_type': 'file_type',
        'risky': 'risky',
        'scan_type': 'scan_type'
    }

    def __init__(self, file_id_list=None, file_name=None, file_type=None, risky=None, scan_type=None):
        r"""IacRequestInfo

        The model defined in huaweicloud sdk

        :param file_id_list: **参数解释**: IaC文件ID列表 **约束限制**: 不涉及 **取值范围**: 1-200个items **默认取值**: 不涉及 
        :type file_id_list: list[str]
        :param file_name: **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 
        :type file_name: str
        :param file_type: **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件。 - k8s_yaml：k8s yaml文件。  **默认取值**: 不涉及 
        :type file_type: str
        :param risky: **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险。 - false：无风险。  **默认取值**: 不涉及 
        :type risky: bool
        :param scan_type: **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描。 - cicd_scan：cicd扫描。  **默认取值**: manual_scan 
        :type scan_type: str
        """
        
        

        self._file_id_list = None
        self._file_name = None
        self._file_type = None
        self._risky = None
        self._scan_type = None
        self.discriminator = None

        if file_id_list is not None:
            self.file_id_list = file_id_list
        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if risky is not None:
            self.risky = risky
        if scan_type is not None:
            self.scan_type = scan_type

    @property
    def file_id_list(self):
        r"""Gets the file_id_list of this IacRequestInfo.

        **参数解释**: IaC文件ID列表 **约束限制**: 不涉及 **取值范围**: 1-200个items **默认取值**: 不涉及 

        :return: The file_id_list of this IacRequestInfo.
        :rtype: list[str]
        """
        return self._file_id_list

    @file_id_list.setter
    def file_id_list(self, file_id_list):
        r"""Sets the file_id_list of this IacRequestInfo.

        **参数解释**: IaC文件ID列表 **约束限制**: 不涉及 **取值范围**: 1-200个items **默认取值**: 不涉及 

        :param file_id_list: The file_id_list of this IacRequestInfo.
        :type file_id_list: list[str]
        """
        self._file_id_list = file_id_list

    @property
    def file_name(self):
        r"""Gets the file_name of this IacRequestInfo.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 

        :return: The file_name of this IacRequestInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this IacRequestInfo.

        **参数解释**: 文件名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64 **默认取值**: 不涉及 

        :param file_name: The file_name of this IacRequestInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this IacRequestInfo.

        **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件。 - k8s_yaml：k8s yaml文件。  **默认取值**: 不涉及 

        :return: The file_type of this IacRequestInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this IacRequestInfo.

        **参数解释**: 文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件。 - k8s_yaml：k8s yaml文件。  **默认取值**: 不涉及 

        :param file_type: The file_type of this IacRequestInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def risky(self):
        r"""Gets the risky of this IacRequestInfo.

        **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险。 - false：无风险。  **默认取值**: 不涉及 

        :return: The risky of this IacRequestInfo.
        :rtype: bool
        """
        return self._risky

    @risky.setter
    def risky(self, risky):
        r"""Sets the risky of this IacRequestInfo.

        **参数解释**: 是否有风险 **约束限制**: 不涉及 **取值范围**: - true：有风险。 - false：无风险。  **默认取值**: 不涉及 

        :param risky: The risky of this IacRequestInfo.
        :type risky: bool
        """
        self._risky = risky

    @property
    def scan_type(self):
        r"""Gets the scan_type of this IacRequestInfo.

        **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描。 - cicd_scan：cicd扫描。  **默认取值**: manual_scan 

        :return: The scan_type of this IacRequestInfo.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this IacRequestInfo.

        **参数解释**: 扫描方式 **约束限制**: 不涉及 **取值范围**: - manual_scan：手动扫描。 - cicd_scan：cicd扫描。  **默认取值**: manual_scan 

        :param scan_type: The scan_type of this IacRequestInfo.
        :type scan_type: str
        """
        self._scan_type = scan_type

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
        if not isinstance(other, IacRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
