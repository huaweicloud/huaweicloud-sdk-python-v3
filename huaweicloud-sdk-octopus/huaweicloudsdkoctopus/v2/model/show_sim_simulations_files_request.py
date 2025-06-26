# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSimSimulationsFilesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, id=None, type=None):
        r"""ShowSimSimulationsFilesRequest

        The model defined in huaweicloud sdk

        :param id: A unique integer value identifying this simulation.
        :type id: int
        :param type: 获取的文件类型  * &#x60;algorithm_log&#x60; - 算法日志文件 * &#x60;algorithm_pb&#x60; - 算法pb文件 * &#x60;algorithm_meta&#x60; - 算法pb文件元数据 * &#x60;sim_osi&#x60; - 仿真pb文件 * &#x60;osi_meta&#x60; - 仿真pb文件元数据 * &#x60;evaluation&#x60; - 评测pb文件 * &#x60;evaluation_log&#x60; - 评测日志文件
        :type type: str
        """
        
        

        self._id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.type = type

    @property
    def id(self):
        r"""Gets the id of this ShowSimSimulationsFilesRequest.

        A unique integer value identifying this simulation.

        :return: The id of this ShowSimSimulationsFilesRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSimSimulationsFilesRequest.

        A unique integer value identifying this simulation.

        :param id: The id of this ShowSimSimulationsFilesRequest.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowSimSimulationsFilesRequest.

        获取的文件类型  * `algorithm_log` - 算法日志文件 * `algorithm_pb` - 算法pb文件 * `algorithm_meta` - 算法pb文件元数据 * `sim_osi` - 仿真pb文件 * `osi_meta` - 仿真pb文件元数据 * `evaluation` - 评测pb文件 * `evaluation_log` - 评测日志文件

        :return: The type of this ShowSimSimulationsFilesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowSimSimulationsFilesRequest.

        获取的文件类型  * `algorithm_log` - 算法日志文件 * `algorithm_pb` - 算法pb文件 * `algorithm_meta` - 算法pb文件元数据 * `sim_osi` - 仿真pb文件 * `osi_meta` - 仿真pb文件元数据 * `evaluation` - 评测pb文件 * `evaluation_log` - 评测日志文件

        :param type: The type of this ShowSimSimulationsFilesRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowSimSimulationsFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
