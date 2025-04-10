# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditOperateLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'operate_log': 'list[OperateLogInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'operate_log': 'operate_log'
    }

    def __init__(self, total_num=None, operate_log=None):
        r"""ListAuditOperateLogsResponse

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param operate_log: 操作日志列表
        :type operate_log: list[:class:`huaweicloudsdkdbss.v1.OperateLogInfo`]
        """
        
        super(ListAuditOperateLogsResponse, self).__init__()

        self._total_num = None
        self._operate_log = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if operate_log is not None:
            self.operate_log = operate_log

    @property
    def total_num(self):
        r"""Gets the total_num of this ListAuditOperateLogsResponse.

        总数

        :return: The total_num of this ListAuditOperateLogsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListAuditOperateLogsResponse.

        总数

        :param total_num: The total_num of this ListAuditOperateLogsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def operate_log(self):
        r"""Gets the operate_log of this ListAuditOperateLogsResponse.

        操作日志列表

        :return: The operate_log of this ListAuditOperateLogsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.OperateLogInfo`]
        """
        return self._operate_log

    @operate_log.setter
    def operate_log(self, operate_log):
        r"""Sets the operate_log of this ListAuditOperateLogsResponse.

        操作日志列表

        :param operate_log: The operate_log of this ListAuditOperateLogsResponse.
        :type operate_log: list[:class:`huaweicloudsdkdbss.v1.OperateLogInfo`]
        """
        self._operate_log = operate_log

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
        if not isinstance(other, ListAuditOperateLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
