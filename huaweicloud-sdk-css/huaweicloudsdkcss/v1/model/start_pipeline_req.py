# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartPipelineReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_alive': 'bool',
        'names': 'list[str]'
    }

    attribute_map = {
        'keep_alive': 'keepAlive',
        'names': 'names'
    }

    def __init__(self, keep_alive=None, names=None):
        """StartPipelineReq

        The model defined in huaweicloud sdk

        :param keep_alive: 是否保持常驻。   - true: 开启保持常驻。  - false: 关闭保持常驻。  开启“保持常驻”适用于需要长期运行的业务。开启“保持常驻”以后，将会在每个节点上面配置一个守护进程，当logstash服务出现故障的时候，会主动拉起并修复。“保持常驻”不适用于短期运行的业务，因为多次主动拉起logstash服务会导致数据迁移重复。
        :type keep_alive: bool
        :param names: 配置文件名称。
        :type names: list[str]
        """
        
        

        self._keep_alive = None
        self._names = None
        self.discriminator = None

        if keep_alive is not None:
            self.keep_alive = keep_alive
        self.names = names

    @property
    def keep_alive(self):
        """Gets the keep_alive of this StartPipelineReq.

        是否保持常驻。   - true: 开启保持常驻。  - false: 关闭保持常驻。  开启“保持常驻”适用于需要长期运行的业务。开启“保持常驻”以后，将会在每个节点上面配置一个守护进程，当logstash服务出现故障的时候，会主动拉起并修复。“保持常驻”不适用于短期运行的业务，因为多次主动拉起logstash服务会导致数据迁移重复。

        :return: The keep_alive of this StartPipelineReq.
        :rtype: bool
        """
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, keep_alive):
        """Sets the keep_alive of this StartPipelineReq.

        是否保持常驻。   - true: 开启保持常驻。  - false: 关闭保持常驻。  开启“保持常驻”适用于需要长期运行的业务。开启“保持常驻”以后，将会在每个节点上面配置一个守护进程，当logstash服务出现故障的时候，会主动拉起并修复。“保持常驻”不适用于短期运行的业务，因为多次主动拉起logstash服务会导致数据迁移重复。

        :param keep_alive: The keep_alive of this StartPipelineReq.
        :type keep_alive: bool
        """
        self._keep_alive = keep_alive

    @property
    def names(self):
        """Gets the names of this StartPipelineReq.

        配置文件名称。

        :return: The names of this StartPipelineReq.
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this StartPipelineReq.

        配置文件名称。

        :param names: The names of this StartPipelineReq.
        :type names: list[str]
        """
        self._names = names

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
        if not isinstance(other, StartPipelineReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
