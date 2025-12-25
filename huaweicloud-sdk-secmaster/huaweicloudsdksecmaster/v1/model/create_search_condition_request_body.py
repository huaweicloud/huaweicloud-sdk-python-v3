# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSearchConditionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_name': 'str',
        'dataspace_id': 'str',
        'pipe_id': 'str',
        'query': 'str'
    }

    attribute_map = {
        'condition_name': 'condition_name',
        'dataspace_id': 'dataspace_id',
        'pipe_id': 'pipe_id',
        'query': 'query'
    }

    def __init__(self, condition_name=None, dataspace_id=None, pipe_id=None, query=None):
        r"""CreateSearchConditionRequestBody

        The model defined in huaweicloud sdk

        :param condition_name: 检索条件名称
        :type condition_name: str
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param pipe_id: 数据管道ID
        :type pipe_id: str
        :param query: 查询语句
        :type query: str
        """
        
        

        self._condition_name = None
        self._dataspace_id = None
        self._pipe_id = None
        self._query = None
        self.discriminator = None

        self.condition_name = condition_name
        self.dataspace_id = dataspace_id
        self.pipe_id = pipe_id
        self.query = query

    @property
    def condition_name(self):
        r"""Gets the condition_name of this CreateSearchConditionRequestBody.

        检索条件名称

        :return: The condition_name of this CreateSearchConditionRequestBody.
        :rtype: str
        """
        return self._condition_name

    @condition_name.setter
    def condition_name(self, condition_name):
        r"""Sets the condition_name of this CreateSearchConditionRequestBody.

        检索条件名称

        :param condition_name: The condition_name of this CreateSearchConditionRequestBody.
        :type condition_name: str
        """
        self._condition_name = condition_name

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this CreateSearchConditionRequestBody.

        数据空间ID

        :return: The dataspace_id of this CreateSearchConditionRequestBody.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this CreateSearchConditionRequestBody.

        数据空间ID

        :param dataspace_id: The dataspace_id of this CreateSearchConditionRequestBody.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this CreateSearchConditionRequestBody.

        数据管道ID

        :return: The pipe_id of this CreateSearchConditionRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this CreateSearchConditionRequestBody.

        数据管道ID

        :param pipe_id: The pipe_id of this CreateSearchConditionRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def query(self):
        r"""Gets the query of this CreateSearchConditionRequestBody.

        查询语句

        :return: The query of this CreateSearchConditionRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateSearchConditionRequestBody.

        查询语句

        :param query: The query of this CreateSearchConditionRequestBody.
        :type query: str
        """
        self._query = query

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
        if not isinstance(other, CreateSearchConditionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
