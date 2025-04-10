# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExerciseCaseResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'polymeric_resource_id': 'str',
        'input_file': 'str',
        'output_file': 'str',
        'index': 'int',
        'input_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'polymeric_resource_id': 'polymeric_resource_id',
        'input_file': 'input_file',
        'output_file': 'output_file',
        'index': 'index',
        'input_type': 'input_type'
    }

    def __init__(self, id=None, polymeric_resource_id=None, input_file=None, output_file=None, index=None, input_type=None):
        r"""ExerciseCaseResource

        The model defined in huaweicloud sdk

        :param id: 测试用例存储id
        :type id: str
        :param polymeric_resource_id: 资源聚合id
        :type polymeric_resource_id: str
        :param input_file: 用例输入
        :type input_file: str
        :param output_file: 用例输出
        :type output_file: str
        :param index: 用例顺序位置
        :type index: int
        :param input_type: 用例类型
        :type input_type: str
        """
        
        

        self._id = None
        self._polymeric_resource_id = None
        self._input_file = None
        self._output_file = None
        self._index = None
        self._input_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if polymeric_resource_id is not None:
            self.polymeric_resource_id = polymeric_resource_id
        if input_file is not None:
            self.input_file = input_file
        if output_file is not None:
            self.output_file = output_file
        if index is not None:
            self.index = index
        if input_type is not None:
            self.input_type = input_type

    @property
    def id(self):
        r"""Gets the id of this ExerciseCaseResource.

        测试用例存储id

        :return: The id of this ExerciseCaseResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExerciseCaseResource.

        测试用例存储id

        :param id: The id of this ExerciseCaseResource.
        :type id: str
        """
        self._id = id

    @property
    def polymeric_resource_id(self):
        r"""Gets the polymeric_resource_id of this ExerciseCaseResource.

        资源聚合id

        :return: The polymeric_resource_id of this ExerciseCaseResource.
        :rtype: str
        """
        return self._polymeric_resource_id

    @polymeric_resource_id.setter
    def polymeric_resource_id(self, polymeric_resource_id):
        r"""Sets the polymeric_resource_id of this ExerciseCaseResource.

        资源聚合id

        :param polymeric_resource_id: The polymeric_resource_id of this ExerciseCaseResource.
        :type polymeric_resource_id: str
        """
        self._polymeric_resource_id = polymeric_resource_id

    @property
    def input_file(self):
        r"""Gets the input_file of this ExerciseCaseResource.

        用例输入

        :return: The input_file of this ExerciseCaseResource.
        :rtype: str
        """
        return self._input_file

    @input_file.setter
    def input_file(self, input_file):
        r"""Sets the input_file of this ExerciseCaseResource.

        用例输入

        :param input_file: The input_file of this ExerciseCaseResource.
        :type input_file: str
        """
        self._input_file = input_file

    @property
    def output_file(self):
        r"""Gets the output_file of this ExerciseCaseResource.

        用例输出

        :return: The output_file of this ExerciseCaseResource.
        :rtype: str
        """
        return self._output_file

    @output_file.setter
    def output_file(self, output_file):
        r"""Sets the output_file of this ExerciseCaseResource.

        用例输出

        :param output_file: The output_file of this ExerciseCaseResource.
        :type output_file: str
        """
        self._output_file = output_file

    @property
    def index(self):
        r"""Gets the index of this ExerciseCaseResource.

        用例顺序位置

        :return: The index of this ExerciseCaseResource.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this ExerciseCaseResource.

        用例顺序位置

        :param index: The index of this ExerciseCaseResource.
        :type index: int
        """
        self._index = index

    @property
    def input_type(self):
        r"""Gets the input_type of this ExerciseCaseResource.

        用例类型

        :return: The input_type of this ExerciseCaseResource.
        :rtype: str
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        r"""Sets the input_type of this ExerciseCaseResource.

        用例类型

        :param input_type: The input_type of this ExerciseCaseResource.
        :type input_type: str
        """
        self._input_type = input_type

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
        if not isinstance(other, ExerciseCaseResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
