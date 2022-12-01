# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncCommitJobResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'async_job_id': 'str',
        'status': 'str',
        'msg': 'str'
    }

    attribute_map = {
        'async_job_id': 'async_job_id',
        'status': 'status',
        'msg': 'msg'
    }

    def __init__(self, async_job_id=None, status=None, msg=None):
        """AsyncCommitJobResp

        The model defined in huaweicloud sdk

        :param async_job_id: 批量异步任务ID。
        :type async_job_id: str
        :param status: 批量异步任务状态。
        :type status: str
        :param msg: 提交指定ID批量异步任务结果信息。
        :type msg: str
        """
        
        

        self._async_job_id = None
        self._status = None
        self._msg = None
        self.discriminator = None

        self.async_job_id = async_job_id
        self.status = status
        self.msg = msg

    @property
    def async_job_id(self):
        """Gets the async_job_id of this AsyncCommitJobResp.

        批量异步任务ID。

        :return: The async_job_id of this AsyncCommitJobResp.
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        """Sets the async_job_id of this AsyncCommitJobResp.

        批量异步任务ID。

        :param async_job_id: The async_job_id of this AsyncCommitJobResp.
        :type async_job_id: str
        """
        self._async_job_id = async_job_id

    @property
    def status(self):
        """Gets the status of this AsyncCommitJobResp.

        批量异步任务状态。

        :return: The status of this AsyncCommitJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AsyncCommitJobResp.

        批量异步任务状态。

        :param status: The status of this AsyncCommitJobResp.
        :type status: str
        """
        self._status = status

    @property
    def msg(self):
        """Gets the msg of this AsyncCommitJobResp.

        提交指定ID批量异步任务结果信息。

        :return: The msg of this AsyncCommitJobResp.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this AsyncCommitJobResp.

        提交指定ID批量异步任务结果信息。

        :param msg: The msg of this AsyncCommitJobResp.
        :type msg: str
        """
        self._msg = msg

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
        if not isinstance(other, AsyncCommitJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
