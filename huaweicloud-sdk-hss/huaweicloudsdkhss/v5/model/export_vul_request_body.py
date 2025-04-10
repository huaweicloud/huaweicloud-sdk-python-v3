# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportVulRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_headers': 'list[list[str]]',
        'vul_id_list': 'list[str]',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'export_headers': 'export_headers',
        'vul_id_list': 'vul_id_list',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, export_headers=None, vul_id_list=None, host_id_list=None):
        r"""ExportVulRequestBody

        The model defined in huaweicloud sdk

        :param export_headers: 导出漏洞数据的表头信息列表
        :type export_headers: list[list[str]]
        :param vul_id_list: 指定导出的漏洞id列表
        :type vul_id_list: list[str]
        :param host_id_list: 指定导出的主机id列表
        :type host_id_list: list[str]
        """
        
        

        self._export_headers = None
        self._vul_id_list = None
        self._host_id_list = None
        self.discriminator = None

        if export_headers is not None:
            self.export_headers = export_headers
        if vul_id_list is not None:
            self.vul_id_list = vul_id_list
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def export_headers(self):
        r"""Gets the export_headers of this ExportVulRequestBody.

        导出漏洞数据的表头信息列表

        :return: The export_headers of this ExportVulRequestBody.
        :rtype: list[list[str]]
        """
        return self._export_headers

    @export_headers.setter
    def export_headers(self, export_headers):
        r"""Sets the export_headers of this ExportVulRequestBody.

        导出漏洞数据的表头信息列表

        :param export_headers: The export_headers of this ExportVulRequestBody.
        :type export_headers: list[list[str]]
        """
        self._export_headers = export_headers

    @property
    def vul_id_list(self):
        r"""Gets the vul_id_list of this ExportVulRequestBody.

        指定导出的漏洞id列表

        :return: The vul_id_list of this ExportVulRequestBody.
        :rtype: list[str]
        """
        return self._vul_id_list

    @vul_id_list.setter
    def vul_id_list(self, vul_id_list):
        r"""Sets the vul_id_list of this ExportVulRequestBody.

        指定导出的漏洞id列表

        :param vul_id_list: The vul_id_list of this ExportVulRequestBody.
        :type vul_id_list: list[str]
        """
        self._vul_id_list = vul_id_list

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ExportVulRequestBody.

        指定导出的主机id列表

        :return: The host_id_list of this ExportVulRequestBody.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ExportVulRequestBody.

        指定导出的主机id列表

        :param host_id_list: The host_id_list of this ExportVulRequestBody.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, ExportVulRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
