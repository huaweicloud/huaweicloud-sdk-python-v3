# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartHotPipelineRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'keep_alive': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'keep_alive': 'keep_alive'
    }

    def __init__(self, name=None, keep_alive=None):
        r"""StartHotPipelineRequestBody

        The model defined in huaweicloud sdk

        :param name: 配置文件名称。
        :type name: str
        :param keep_alive: 热启动操作时，需要与集群已存在管道的 “是否保持常驻”值保持一致。 - true: 开启保持常驻。 - false: 关闭保持常驻。 开启“保持常驻”适用于需要长期运行的业务。开启“保持常驻”以后，将会在每个节点上面配置一个守护进程，当logstash服务出现故障的时候，会主动拉起并修复。“保持常驻”不适用于短期运行的业务，因为多次主动拉起logstash服务会导致数据迁移重复。
        :type keep_alive: bool
        """
        
        

        self._name = None
        self._keep_alive = None
        self.discriminator = None

        self.name = name
        if keep_alive is not None:
            self.keep_alive = keep_alive

    @property
    def name(self):
        r"""Gets the name of this StartHotPipelineRequestBody.

        配置文件名称。

        :return: The name of this StartHotPipelineRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StartHotPipelineRequestBody.

        配置文件名称。

        :param name: The name of this StartHotPipelineRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def keep_alive(self):
        r"""Gets the keep_alive of this StartHotPipelineRequestBody.

        热启动操作时，需要与集群已存在管道的 “是否保持常驻”值保持一致。 - true: 开启保持常驻。 - false: 关闭保持常驻。 开启“保持常驻”适用于需要长期运行的业务。开启“保持常驻”以后，将会在每个节点上面配置一个守护进程，当logstash服务出现故障的时候，会主动拉起并修复。“保持常驻”不适用于短期运行的业务，因为多次主动拉起logstash服务会导致数据迁移重复。

        :return: The keep_alive of this StartHotPipelineRequestBody.
        :rtype: bool
        """
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, keep_alive):
        r"""Sets the keep_alive of this StartHotPipelineRequestBody.

        热启动操作时，需要与集群已存在管道的 “是否保持常驻”值保持一致。 - true: 开启保持常驻。 - false: 关闭保持常驻。 开启“保持常驻”适用于需要长期运行的业务。开启“保持常驻”以后，将会在每个节点上面配置一个守护进程，当logstash服务出现故障的时候，会主动拉起并修复。“保持常驻”不适用于短期运行的业务，因为多次主动拉起logstash服务会导致数据迁移重复。

        :param keep_alive: The keep_alive of this StartHotPipelineRequestBody.
        :type keep_alive: bool
        """
        self._keep_alive = keep_alive

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StartHotPipelineRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
