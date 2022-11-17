# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobid': 'str'
    }

    attribute_map = {
        'jobid': 'jobid'
    }

    def __init__(self, jobid=None):
        """ResetNodeResponse

        The model defined in huaweicloud sdk

        :param jobid: 提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。
        :type jobid: str
        """
        
        super(ResetNodeResponse, self).__init__()

        self._jobid = None
        self.discriminator = None

        if jobid is not None:
            self.jobid = jobid

    @property
    def jobid(self):
        """Gets the jobid of this ResetNodeResponse.

        提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。

        :return: The jobid of this ResetNodeResponse.
        :rtype: str
        """
        return self._jobid

    @jobid.setter
    def jobid(self, jobid):
        """Sets the jobid of this ResetNodeResponse.

        提交任务成功后返回的任务ID，用户可以使用该ID对任务执行情况进行查询。

        :param jobid: The jobid of this ResetNodeResponse.
        :type jobid: str
        """
        self._jobid = jobid

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
        if not isinstance(other, ResetNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
