# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportRisksRequestBody:

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
        'iac_items': 'IacRequestInfo'
    }

    attribute_map = {
        'export_headers': 'export_headers',
        'iac_items': 'iac_items'
    }

    def __init__(self, export_headers=None, iac_items=None):
        r"""ExportRisksRequestBody

        The model defined in huaweicloud sdk

        :param export_headers: **参数解释**: 导出集群环境安全数据的表头信息列表 **取值范围**: 最小值1，最大值10000 
        :type export_headers: list[list[str]]
        :param iac_items: 
        :type iac_items: :class:`huaweicloudsdkhss.v5.IacRequestInfo`
        """
        
        

        self._export_headers = None
        self._iac_items = None
        self.discriminator = None

        self.export_headers = export_headers
        if iac_items is not None:
            self.iac_items = iac_items

    @property
    def export_headers(self):
        r"""Gets the export_headers of this ExportRisksRequestBody.

        **参数解释**: 导出集群环境安全数据的表头信息列表 **取值范围**: 最小值1，最大值10000 

        :return: The export_headers of this ExportRisksRequestBody.
        :rtype: list[list[str]]
        """
        return self._export_headers

    @export_headers.setter
    def export_headers(self, export_headers):
        r"""Sets the export_headers of this ExportRisksRequestBody.

        **参数解释**: 导出集群环境安全数据的表头信息列表 **取值范围**: 最小值1，最大值10000 

        :param export_headers: The export_headers of this ExportRisksRequestBody.
        :type export_headers: list[list[str]]
        """
        self._export_headers = export_headers

    @property
    def iac_items(self):
        r"""Gets the iac_items of this ExportRisksRequestBody.

        :return: The iac_items of this ExportRisksRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.IacRequestInfo`
        """
        return self._iac_items

    @iac_items.setter
    def iac_items(self, iac_items):
        r"""Sets the iac_items of this ExportRisksRequestBody.

        :param iac_items: The iac_items of this ExportRisksRequestBody.
        :type iac_items: :class:`huaweicloudsdkhss.v5.IacRequestInfo`
        """
        self._iac_items = iac_items

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
        if not isinstance(other, ExportRisksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
