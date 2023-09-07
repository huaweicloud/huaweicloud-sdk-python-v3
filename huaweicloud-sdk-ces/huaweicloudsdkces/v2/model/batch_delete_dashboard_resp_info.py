# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteDashboardRespInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dashboard_id': 'str',
        'ret_status': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'dashboard_id': 'dashboard_id',
        'ret_status': 'ret_status',
        'error_msg': 'error_msg'
    }

    def __init__(self, dashboard_id=None, ret_status=None, error_msg=None):
        """BatchDeleteDashboardRespInfo

        The model defined in huaweicloud sdk

        :param dashboard_id: 监控看板id
        :type dashboard_id: str
        :param ret_status: 处理结果, successful: 成功, error: 失败
        :type ret_status: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._dashboard_id = None
        self._ret_status = None
        self._error_msg = None
        self.discriminator = None

        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if ret_status is not None:
            self.ret_status = ret_status
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this BatchDeleteDashboardRespInfo.

        监控看板id

        :return: The dashboard_id of this BatchDeleteDashboardRespInfo.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this BatchDeleteDashboardRespInfo.

        监控看板id

        :param dashboard_id: The dashboard_id of this BatchDeleteDashboardRespInfo.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def ret_status(self):
        """Gets the ret_status of this BatchDeleteDashboardRespInfo.

        处理结果, successful: 成功, error: 失败

        :return: The ret_status of this BatchDeleteDashboardRespInfo.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        """Sets the ret_status of this BatchDeleteDashboardRespInfo.

        处理结果, successful: 成功, error: 失败

        :param ret_status: The ret_status of this BatchDeleteDashboardRespInfo.
        :type ret_status: str
        """
        self._ret_status = ret_status

    @property
    def error_msg(self):
        """Gets the error_msg of this BatchDeleteDashboardRespInfo.

        错误信息

        :return: The error_msg of this BatchDeleteDashboardRespInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this BatchDeleteDashboardRespInfo.

        错误信息

        :param error_msg: The error_msg of this BatchDeleteDashboardRespInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, BatchDeleteDashboardRespInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
