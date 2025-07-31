# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksResponseInfoClusterScanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_type_list': 'list[str]',
        'scanning_cluster_num': 'int',
        'success_cluster_num': 'int',
        'failed_cluster_num': 'int'
    }

    attribute_map = {
        'scan_type_list': 'scan_type_list',
        'scanning_cluster_num': 'scanning_cluster_num',
        'success_cluster_num': 'success_cluster_num',
        'failed_cluster_num': 'failed_cluster_num'
    }

    def __init__(self, scan_type_list=None, scanning_cluster_num=None, success_cluster_num=None, failed_cluster_num=None):
        r"""ListTasksResponseInfoClusterScanInfo

        The model defined in huaweicloud sdk

        :param scan_type_list: 本次扫描任务涉及的扫描项类型列表
        :type scan_type_list: list[str]
        :param scanning_cluster_num: 当前任务处于扫描中的集群数量
        :type scanning_cluster_num: int
        :param success_cluster_num: 当前任务扫描成功的集群数量
        :type success_cluster_num: int
        :param failed_cluster_num: 当前任务扫描失败的集群数量
        :type failed_cluster_num: int
        """
        
        

        self._scan_type_list = None
        self._scanning_cluster_num = None
        self._success_cluster_num = None
        self._failed_cluster_num = None
        self.discriminator = None

        if scan_type_list is not None:
            self.scan_type_list = scan_type_list
        if scanning_cluster_num is not None:
            self.scanning_cluster_num = scanning_cluster_num
        if success_cluster_num is not None:
            self.success_cluster_num = success_cluster_num
        if failed_cluster_num is not None:
            self.failed_cluster_num = failed_cluster_num

    @property
    def scan_type_list(self):
        r"""Gets the scan_type_list of this ListTasksResponseInfoClusterScanInfo.

        本次扫描任务涉及的扫描项类型列表

        :return: The scan_type_list of this ListTasksResponseInfoClusterScanInfo.
        :rtype: list[str]
        """
        return self._scan_type_list

    @scan_type_list.setter
    def scan_type_list(self, scan_type_list):
        r"""Sets the scan_type_list of this ListTasksResponseInfoClusterScanInfo.

        本次扫描任务涉及的扫描项类型列表

        :param scan_type_list: The scan_type_list of this ListTasksResponseInfoClusterScanInfo.
        :type scan_type_list: list[str]
        """
        self._scan_type_list = scan_type_list

    @property
    def scanning_cluster_num(self):
        r"""Gets the scanning_cluster_num of this ListTasksResponseInfoClusterScanInfo.

        当前任务处于扫描中的集群数量

        :return: The scanning_cluster_num of this ListTasksResponseInfoClusterScanInfo.
        :rtype: int
        """
        return self._scanning_cluster_num

    @scanning_cluster_num.setter
    def scanning_cluster_num(self, scanning_cluster_num):
        r"""Sets the scanning_cluster_num of this ListTasksResponseInfoClusterScanInfo.

        当前任务处于扫描中的集群数量

        :param scanning_cluster_num: The scanning_cluster_num of this ListTasksResponseInfoClusterScanInfo.
        :type scanning_cluster_num: int
        """
        self._scanning_cluster_num = scanning_cluster_num

    @property
    def success_cluster_num(self):
        r"""Gets the success_cluster_num of this ListTasksResponseInfoClusterScanInfo.

        当前任务扫描成功的集群数量

        :return: The success_cluster_num of this ListTasksResponseInfoClusterScanInfo.
        :rtype: int
        """
        return self._success_cluster_num

    @success_cluster_num.setter
    def success_cluster_num(self, success_cluster_num):
        r"""Sets the success_cluster_num of this ListTasksResponseInfoClusterScanInfo.

        当前任务扫描成功的集群数量

        :param success_cluster_num: The success_cluster_num of this ListTasksResponseInfoClusterScanInfo.
        :type success_cluster_num: int
        """
        self._success_cluster_num = success_cluster_num

    @property
    def failed_cluster_num(self):
        r"""Gets the failed_cluster_num of this ListTasksResponseInfoClusterScanInfo.

        当前任务扫描失败的集群数量

        :return: The failed_cluster_num of this ListTasksResponseInfoClusterScanInfo.
        :rtype: int
        """
        return self._failed_cluster_num

    @failed_cluster_num.setter
    def failed_cluster_num(self, failed_cluster_num):
        r"""Sets the failed_cluster_num of this ListTasksResponseInfoClusterScanInfo.

        当前任务扫描失败的集群数量

        :param failed_cluster_num: The failed_cluster_num of this ListTasksResponseInfoClusterScanInfo.
        :type failed_cluster_num: int
        """
        self._failed_cluster_num = failed_cluster_num

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
        if not isinstance(other, ListTasksResponseInfoClusterScanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
