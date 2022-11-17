# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchQueryParamReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[str]',
        'refresh': 'str'
    }

    attribute_map = {
        'jobs': 'jobs',
        'refresh': 'refresh'
    }

    def __init__(self, jobs=None, refresh=None):
        """BatchQueryParamReq

        The model defined in huaweicloud sdk

        :param jobs: 查询任务ID集合。
        :type jobs: list[str]
        :param refresh: 是否重新获取数据库参数，1代表是，0代表否（从缓存中获取），第一次调用时请设置为1。
        :type refresh: str
        """
        
        

        self._jobs = None
        self._refresh = None
        self.discriminator = None

        self.jobs = jobs
        self.refresh = refresh

    @property
    def jobs(self):
        """Gets the jobs of this BatchQueryParamReq.

        查询任务ID集合。

        :return: The jobs of this BatchQueryParamReq.
        :rtype: list[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this BatchQueryParamReq.

        查询任务ID集合。

        :param jobs: The jobs of this BatchQueryParamReq.
        :type jobs: list[str]
        """
        self._jobs = jobs

    @property
    def refresh(self):
        """Gets the refresh of this BatchQueryParamReq.

        是否重新获取数据库参数，1代表是，0代表否（从缓存中获取），第一次调用时请设置为1。

        :return: The refresh of this BatchQueryParamReq.
        :rtype: str
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this BatchQueryParamReq.

        是否重新获取数据库参数，1代表是，0代表否（从缓存中获取），第一次调用时请设置为1。

        :param refresh: The refresh of this BatchQueryParamReq.
        :type refresh: str
        """
        self._refresh = refresh

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
        if not isinstance(other, BatchQueryParamReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
