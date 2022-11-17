# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryStructDetailResp:

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
        'error_code': 'str',
        'error_message': 'str',
        'struct_detail': 'QueryFlowCompareDataResp'
    }

    attribute_map = {
        'job_id': 'job_id',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'struct_detail': 'struct_detail'
    }

    def __init__(self, job_id=None, error_code=None, error_message=None, struct_detail=None):
        """QueryStructDetailResp

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param error_code: 错误码
        :type error_code: str
        :param error_message: 错误信息
        :type error_message: str
        :param struct_detail: 
        :type struct_detail: :class:`huaweicloudsdkdrs.v3.QueryFlowCompareDataResp`
        """
        
        

        self._job_id = None
        self._error_code = None
        self._error_message = None
        self._struct_detail = None
        self.discriminator = None

        self.job_id = job_id
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if struct_detail is not None:
            self.struct_detail = struct_detail

    @property
    def job_id(self):
        """Gets the job_id of this QueryStructDetailResp.

        任务ID

        :return: The job_id of this QueryStructDetailResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QueryStructDetailResp.

        任务ID

        :param job_id: The job_id of this QueryStructDetailResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def error_code(self):
        """Gets the error_code of this QueryStructDetailResp.

        错误码

        :return: The error_code of this QueryStructDetailResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryStructDetailResp.

        错误码

        :param error_code: The error_code of this QueryStructDetailResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this QueryStructDetailResp.

        错误信息

        :return: The error_message of this QueryStructDetailResp.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this QueryStructDetailResp.

        错误信息

        :param error_message: The error_message of this QueryStructDetailResp.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def struct_detail(self):
        """Gets the struct_detail of this QueryStructDetailResp.

        :return: The struct_detail of this QueryStructDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.QueryFlowCompareDataResp`
        """
        return self._struct_detail

    @struct_detail.setter
    def struct_detail(self, struct_detail):
        """Sets the struct_detail of this QueryStructDetailResp.

        :param struct_detail: The struct_detail of this QueryStructDetailResp.
        :type struct_detail: :class:`huaweicloudsdkdrs.v3.QueryFlowCompareDataResp`
        """
        self._struct_detail = struct_detail

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
        if not isinstance(other, QueryStructDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
