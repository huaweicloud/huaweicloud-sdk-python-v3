# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsScanResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'db_scan_results': 'list[ObsScanResultInfo]'
    }

    attribute_map = {
        'total': 'total',
        'db_scan_results': 'db_scan_results'
    }

    def __init__(self, total=None, db_scan_results=None):
        """ObsScanResult

        The model defined in huaweicloud sdk

        :param total: 扫描结果总数
        :type total: int
        :param db_scan_results: OBS扫描结果列表
        :type db_scan_results: list[:class:`huaweicloudsdkdsc.v1.ObsScanResultInfo`]
        """
        
        

        self._total = None
        self._db_scan_results = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if db_scan_results is not None:
            self.db_scan_results = db_scan_results

    @property
    def total(self):
        """Gets the total of this ObsScanResult.

        扫描结果总数

        :return: The total of this ObsScanResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ObsScanResult.

        扫描结果总数

        :param total: The total of this ObsScanResult.
        :type total: int
        """
        self._total = total

    @property
    def db_scan_results(self):
        """Gets the db_scan_results of this ObsScanResult.

        OBS扫描结果列表

        :return: The db_scan_results of this ObsScanResult.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.ObsScanResultInfo`]
        """
        return self._db_scan_results

    @db_scan_results.setter
    def db_scan_results(self, db_scan_results):
        """Sets the db_scan_results of this ObsScanResult.

        OBS扫描结果列表

        :param db_scan_results: The db_scan_results of this ObsScanResult.
        :type db_scan_results: list[:class:`huaweicloudsdkdsc.v1.ObsScanResultInfo`]
        """
        self._db_scan_results = db_scan_results

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
        if not isinstance(other, ObsScanResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
