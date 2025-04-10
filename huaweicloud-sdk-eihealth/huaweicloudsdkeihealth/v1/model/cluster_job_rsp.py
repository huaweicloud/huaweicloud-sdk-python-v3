# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterJobRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'method': 'str',
        'output_dir': 'str',
        'status': 'str',
        'failed_reasons': 'list[FailedReasonRecord]'
    }

    attribute_map = {
        'method': 'method',
        'output_dir': 'output_dir',
        'status': 'status',
        'failed_reasons': 'failed_reasons'
    }

    def __init__(self, method=None, output_dir=None, status=None, failed_reasons=None):
        r"""ClusterJobRsp

        The model defined in huaweicloud sdk

        :param method: 分子聚类方法
        :type method: str
        :param output_dir: 分子聚类输出结果
        :type output_dir: str
        :param status: 作业结果信息
        :type status: str
        :param failed_reasons: 部分失败原因和数量
        :type failed_reasons: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        
        

        self._method = None
        self._output_dir = None
        self._status = None
        self._failed_reasons = None
        self.discriminator = None

        self.method = method
        self.output_dir = output_dir
        self.status = status
        self.failed_reasons = failed_reasons

    @property
    def method(self):
        r"""Gets the method of this ClusterJobRsp.

        分子聚类方法

        :return: The method of this ClusterJobRsp.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this ClusterJobRsp.

        分子聚类方法

        :param method: The method of this ClusterJobRsp.
        :type method: str
        """
        self._method = method

    @property
    def output_dir(self):
        r"""Gets the output_dir of this ClusterJobRsp.

        分子聚类输出结果

        :return: The output_dir of this ClusterJobRsp.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        r"""Sets the output_dir of this ClusterJobRsp.

        分子聚类输出结果

        :param output_dir: The output_dir of this ClusterJobRsp.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def status(self):
        r"""Gets the status of this ClusterJobRsp.

        作业结果信息

        :return: The status of this ClusterJobRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterJobRsp.

        作业结果信息

        :param status: The status of this ClusterJobRsp.
        :type status: str
        """
        self._status = status

    @property
    def failed_reasons(self):
        r"""Gets the failed_reasons of this ClusterJobRsp.

        部分失败原因和数量

        :return: The failed_reasons of this ClusterJobRsp.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        r"""Sets the failed_reasons of this ClusterJobRsp.

        部分失败原因和数量

        :param failed_reasons: The failed_reasons of this ClusterJobRsp.
        :type failed_reasons: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        self._failed_reasons = failed_reasons

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
        if not isinstance(other, ClusterJobRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
