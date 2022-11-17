# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRpoAndRtoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'rpo_info': 'RpoAndRtoInfo',
        'rto_info': 'RpoAndRtoInfo',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'rpo_info': 'rpo_info',
        'rto_info': 'rto_info',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, job_id=None, rpo_info=None, rto_info=None, error_code=None, error_msg=None):
        """QueryRpoAndRtoResp

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param rpo_info: 
        :type rpo_info: :class:`huaweicloudsdkdrs.v3.RpoAndRtoInfo`
        :param rto_info: 
        :type rto_info: :class:`huaweicloudsdkdrs.v3.RpoAndRtoInfo`
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._job_id = None
        self._rpo_info = None
        self._rto_info = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if rpo_info is not None:
            self.rpo_info = rpo_info
        if rto_info is not None:
            self.rto_info = rto_info
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def job_id(self):
        """Gets the job_id of this QueryRpoAndRtoResp.

        任务ID

        :return: The job_id of this QueryRpoAndRtoResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QueryRpoAndRtoResp.

        任务ID

        :param job_id: The job_id of this QueryRpoAndRtoResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def rpo_info(self):
        """Gets the rpo_info of this QueryRpoAndRtoResp.

        :return: The rpo_info of this QueryRpoAndRtoResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.RpoAndRtoInfo`
        """
        return self._rpo_info

    @rpo_info.setter
    def rpo_info(self, rpo_info):
        """Sets the rpo_info of this QueryRpoAndRtoResp.

        :param rpo_info: The rpo_info of this QueryRpoAndRtoResp.
        :type rpo_info: :class:`huaweicloudsdkdrs.v3.RpoAndRtoInfo`
        """
        self._rpo_info = rpo_info

    @property
    def rto_info(self):
        """Gets the rto_info of this QueryRpoAndRtoResp.

        :return: The rto_info of this QueryRpoAndRtoResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.RpoAndRtoInfo`
        """
        return self._rto_info

    @rto_info.setter
    def rto_info(self, rto_info):
        """Sets the rto_info of this QueryRpoAndRtoResp.

        :param rto_info: The rto_info of this QueryRpoAndRtoResp.
        :type rto_info: :class:`huaweicloudsdkdrs.v3.RpoAndRtoInfo`
        """
        self._rto_info = rto_info

    @property
    def error_code(self):
        """Gets the error_code of this QueryRpoAndRtoResp.

        错误码

        :return: The error_code of this QueryRpoAndRtoResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryRpoAndRtoResp.

        错误码

        :param error_code: The error_code of this QueryRpoAndRtoResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this QueryRpoAndRtoResp.

        错误信息

        :return: The error_msg of this QueryRpoAndRtoResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this QueryRpoAndRtoResp.

        错误信息

        :param error_msg: The error_msg of this QueryRpoAndRtoResp.
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
        if not isinstance(other, QueryRpoAndRtoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
