# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DsExportResultVOData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'group': 'BatchOperationVO',
        'rate': 'str'
    }

    attribute_map = {
        'status': 'status',
        'group': 'group',
        'rate': 'rate'
    }

    def __init__(self, status=None, group=None, rate=None):
        """DsExportResultVOData

        The model defined in huaweicloud sdk

        :param status: 标识本次导出的唯一值，用于查询导入结果。importing(导出中)、fail(导出失败)、success(导出成功)。 枚举值：   - importing: 导出中   - fail: 导出失败   - success: 导出成功 
        :type status: str
        :param group: 
        :type group: :class:`huaweicloudsdkdataartsstudio.v1.BatchOperationVO`
        :param rate: 当前进度。
        :type rate: str
        """
        
        

        self._status = None
        self._group = None
        self._rate = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if group is not None:
            self.group = group
        if rate is not None:
            self.rate = rate

    @property
    def status(self):
        """Gets the status of this DsExportResultVOData.

        标识本次导出的唯一值，用于查询导入结果。importing(导出中)、fail(导出失败)、success(导出成功)。 枚举值：   - importing: 导出中   - fail: 导出失败   - success: 导出成功 

        :return: The status of this DsExportResultVOData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DsExportResultVOData.

        标识本次导出的唯一值，用于查询导入结果。importing(导出中)、fail(导出失败)、success(导出成功)。 枚举值：   - importing: 导出中   - fail: 导出失败   - success: 导出成功 

        :param status: The status of this DsExportResultVOData.
        :type status: str
        """
        self._status = status

    @property
    def group(self):
        """Gets the group of this DsExportResultVOData.

        :return: The group of this DsExportResultVOData.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BatchOperationVO`
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DsExportResultVOData.

        :param group: The group of this DsExportResultVOData.
        :type group: :class:`huaweicloudsdkdataartsstudio.v1.BatchOperationVO`
        """
        self._group = group

    @property
    def rate(self):
        """Gets the rate of this DsExportResultVOData.

        当前进度。

        :return: The rate of this DsExportResultVOData.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this DsExportResultVOData.

        当前进度。

        :param rate: The rate of this DsExportResultVOData.
        :type rate: str
        """
        self._rate = rate

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
        if not isinstance(other, DsExportResultVOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
