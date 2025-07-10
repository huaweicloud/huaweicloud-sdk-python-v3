# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimBatchConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_id': 'int',
        'algorithm_name': 'str',
        'builtins_algorithm': 'bool',
        'custom_evaluation_image_id': 'int',
        'custom_simulator_image_id': 'int',
        'description': 'str',
        'evaluation_id': 'int',
        'evaluation_name': 'str',
        'evaluations': 'list[int]',
        'generalization_id': 'int',
        'group_id': 'int',
        'id': 'int',
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'ordering': 'str',
        'search': 'str',
        'suit_id': 'int',
        'triggerable': 'bool'
    }

    attribute_map = {
        'algorithm_id': 'algorithm_id',
        'algorithm_name': 'algorithm_name',
        'builtins_algorithm': 'builtins_algorithm',
        'custom_evaluation_image_id': 'custom_evaluation_image_id',
        'custom_simulator_image_id': 'custom_simulator_image_id',
        'description': 'description',
        'evaluation_id': 'evaluation_id',
        'evaluation_name': 'evaluation_name',
        'evaluations': 'evaluations',
        'generalization_id': 'generalization_id',
        'group_id': 'group_id',
        'id': 'id',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'ordering': 'ordering',
        'search': 'search',
        'suit_id': 'suit_id',
        'triggerable': 'triggerable'
    }

    def __init__(self, algorithm_id=None, algorithm_name=None, builtins_algorithm=None, custom_evaluation_image_id=None, custom_simulator_image_id=None, description=None, evaluation_id=None, evaluation_name=None, evaluations=None, generalization_id=None, group_id=None, id=None, limit=None, name=None, offset=None, ordering=None, search=None, suit_id=None, triggerable=None):
        r"""ListSimBatchConfigsRequest

        The model defined in huaweicloud sdk

        :param algorithm_id: 算法id
        :type algorithm_id: int
        :param algorithm_name: 算法名称
        :type algorithm_name: str
        :param builtins_algorithm: 仿真器内置算法
        :type builtins_algorithm: bool
        :param custom_evaluation_image_id: 自定义评测镜像id
        :type custom_evaluation_image_id: int
        :param custom_simulator_image_id: 自定义仿真器镜像id
        :type custom_simulator_image_id: int
        :param description: 描述
        :type description: str
        :param evaluation_id: 评测id
        :type evaluation_id: int
        :param evaluation_name: 评测名称
        :type evaluation_name: str
        :param evaluations: 
        :type evaluations: list[int]
        :param generalization_id: 泛化任务id
        :type generalization_id: int
        :param group_id: 场景库id
        :type group_id: int
        :param id: 
        :type id: int
        :param limit: Number of results to return per page.
        :type limit: int
        :param name: 
        :type name: str
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param search: A search term.
        :type search: str
        :param suit_id: 测试套件id
        :type suit_id: int
        :param triggerable: 是否可通过流水线功能触发
        :type triggerable: bool
        """
        
        

        self._algorithm_id = None
        self._algorithm_name = None
        self._builtins_algorithm = None
        self._custom_evaluation_image_id = None
        self._custom_simulator_image_id = None
        self._description = None
        self._evaluation_id = None
        self._evaluation_name = None
        self._evaluations = None
        self._generalization_id = None
        self._group_id = None
        self._id = None
        self._limit = None
        self._name = None
        self._offset = None
        self._ordering = None
        self._search = None
        self._suit_id = None
        self._triggerable = None
        self.discriminator = None

        if algorithm_id is not None:
            self.algorithm_id = algorithm_id
        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        if builtins_algorithm is not None:
            self.builtins_algorithm = builtins_algorithm
        if custom_evaluation_image_id is not None:
            self.custom_evaluation_image_id = custom_evaluation_image_id
        if custom_simulator_image_id is not None:
            self.custom_simulator_image_id = custom_simulator_image_id
        if description is not None:
            self.description = description
        if evaluation_id is not None:
            self.evaluation_id = evaluation_id
        if evaluation_name is not None:
            self.evaluation_name = evaluation_name
        if evaluations is not None:
            self.evaluations = evaluations
        if generalization_id is not None:
            self.generalization_id = generalization_id
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if ordering is not None:
            self.ordering = ordering
        if search is not None:
            self.search = search
        if suit_id is not None:
            self.suit_id = suit_id
        if triggerable is not None:
            self.triggerable = triggerable

    @property
    def algorithm_id(self):
        r"""Gets the algorithm_id of this ListSimBatchConfigsRequest.

        算法id

        :return: The algorithm_id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        r"""Sets the algorithm_id of this ListSimBatchConfigsRequest.

        算法id

        :param algorithm_id: The algorithm_id of this ListSimBatchConfigsRequest.
        :type algorithm_id: int
        """
        self._algorithm_id = algorithm_id

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this ListSimBatchConfigsRequest.

        算法名称

        :return: The algorithm_name of this ListSimBatchConfigsRequest.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this ListSimBatchConfigsRequest.

        算法名称

        :param algorithm_name: The algorithm_name of this ListSimBatchConfigsRequest.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

    @property
    def builtins_algorithm(self):
        r"""Gets the builtins_algorithm of this ListSimBatchConfigsRequest.

        仿真器内置算法

        :return: The builtins_algorithm of this ListSimBatchConfigsRequest.
        :rtype: bool
        """
        return self._builtins_algorithm

    @builtins_algorithm.setter
    def builtins_algorithm(self, builtins_algorithm):
        r"""Sets the builtins_algorithm of this ListSimBatchConfigsRequest.

        仿真器内置算法

        :param builtins_algorithm: The builtins_algorithm of this ListSimBatchConfigsRequest.
        :type builtins_algorithm: bool
        """
        self._builtins_algorithm = builtins_algorithm

    @property
    def custom_evaluation_image_id(self):
        r"""Gets the custom_evaluation_image_id of this ListSimBatchConfigsRequest.

        自定义评测镜像id

        :return: The custom_evaluation_image_id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._custom_evaluation_image_id

    @custom_evaluation_image_id.setter
    def custom_evaluation_image_id(self, custom_evaluation_image_id):
        r"""Sets the custom_evaluation_image_id of this ListSimBatchConfigsRequest.

        自定义评测镜像id

        :param custom_evaluation_image_id: The custom_evaluation_image_id of this ListSimBatchConfigsRequest.
        :type custom_evaluation_image_id: int
        """
        self._custom_evaluation_image_id = custom_evaluation_image_id

    @property
    def custom_simulator_image_id(self):
        r"""Gets the custom_simulator_image_id of this ListSimBatchConfigsRequest.

        自定义仿真器镜像id

        :return: The custom_simulator_image_id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._custom_simulator_image_id

    @custom_simulator_image_id.setter
    def custom_simulator_image_id(self, custom_simulator_image_id):
        r"""Sets the custom_simulator_image_id of this ListSimBatchConfigsRequest.

        自定义仿真器镜像id

        :param custom_simulator_image_id: The custom_simulator_image_id of this ListSimBatchConfigsRequest.
        :type custom_simulator_image_id: int
        """
        self._custom_simulator_image_id = custom_simulator_image_id

    @property
    def description(self):
        r"""Gets the description of this ListSimBatchConfigsRequest.

        描述

        :return: The description of this ListSimBatchConfigsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListSimBatchConfigsRequest.

        描述

        :param description: The description of this ListSimBatchConfigsRequest.
        :type description: str
        """
        self._description = description

    @property
    def evaluation_id(self):
        r"""Gets the evaluation_id of this ListSimBatchConfigsRequest.

        评测id

        :return: The evaluation_id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._evaluation_id

    @evaluation_id.setter
    def evaluation_id(self, evaluation_id):
        r"""Sets the evaluation_id of this ListSimBatchConfigsRequest.

        评测id

        :param evaluation_id: The evaluation_id of this ListSimBatchConfigsRequest.
        :type evaluation_id: int
        """
        self._evaluation_id = evaluation_id

    @property
    def evaluation_name(self):
        r"""Gets the evaluation_name of this ListSimBatchConfigsRequest.

        评测名称

        :return: The evaluation_name of this ListSimBatchConfigsRequest.
        :rtype: str
        """
        return self._evaluation_name

    @evaluation_name.setter
    def evaluation_name(self, evaluation_name):
        r"""Sets the evaluation_name of this ListSimBatchConfigsRequest.

        评测名称

        :param evaluation_name: The evaluation_name of this ListSimBatchConfigsRequest.
        :type evaluation_name: str
        """
        self._evaluation_name = evaluation_name

    @property
    def evaluations(self):
        r"""Gets the evaluations of this ListSimBatchConfigsRequest.

        :return: The evaluations of this ListSimBatchConfigsRequest.
        :rtype: list[int]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        r"""Sets the evaluations of this ListSimBatchConfigsRequest.

        :param evaluations: The evaluations of this ListSimBatchConfigsRequest.
        :type evaluations: list[int]
        """
        self._evaluations = evaluations

    @property
    def generalization_id(self):
        r"""Gets the generalization_id of this ListSimBatchConfigsRequest.

        泛化任务id

        :return: The generalization_id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._generalization_id

    @generalization_id.setter
    def generalization_id(self, generalization_id):
        r"""Sets the generalization_id of this ListSimBatchConfigsRequest.

        泛化任务id

        :param generalization_id: The generalization_id of this ListSimBatchConfigsRequest.
        :type generalization_id: int
        """
        self._generalization_id = generalization_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ListSimBatchConfigsRequest.

        场景库id

        :return: The group_id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListSimBatchConfigsRequest.

        场景库id

        :param group_id: The group_id of this ListSimBatchConfigsRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def id(self):
        r"""Gets the id of this ListSimBatchConfigsRequest.

        :return: The id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSimBatchConfigsRequest.

        :param id: The id of this ListSimBatchConfigsRequest.
        :type id: int
        """
        self._id = id

    @property
    def limit(self):
        r"""Gets the limit of this ListSimBatchConfigsRequest.

        Number of results to return per page.

        :return: The limit of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimBatchConfigsRequest.

        Number of results to return per page.

        :param limit: The limit of this ListSimBatchConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListSimBatchConfigsRequest.

        :return: The name of this ListSimBatchConfigsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSimBatchConfigsRequest.

        :param name: The name of this ListSimBatchConfigsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListSimBatchConfigsRequest.

        The initial index from which to return the results.

        :return: The offset of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimBatchConfigsRequest.

        The initial index from which to return the results.

        :param offset: The offset of this ListSimBatchConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def ordering(self):
        r"""Gets the ordering of this ListSimBatchConfigsRequest.

        Which field to use when ordering the results.

        :return: The ordering of this ListSimBatchConfigsRequest.
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        r"""Sets the ordering of this ListSimBatchConfigsRequest.

        Which field to use when ordering the results.

        :param ordering: The ordering of this ListSimBatchConfigsRequest.
        :type ordering: str
        """
        self._ordering = ordering

    @property
    def search(self):
        r"""Gets the search of this ListSimBatchConfigsRequest.

        A search term.

        :return: The search of this ListSimBatchConfigsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListSimBatchConfigsRequest.

        A search term.

        :param search: The search of this ListSimBatchConfigsRequest.
        :type search: str
        """
        self._search = search

    @property
    def suit_id(self):
        r"""Gets the suit_id of this ListSimBatchConfigsRequest.

        测试套件id

        :return: The suit_id of this ListSimBatchConfigsRequest.
        :rtype: int
        """
        return self._suit_id

    @suit_id.setter
    def suit_id(self, suit_id):
        r"""Sets the suit_id of this ListSimBatchConfigsRequest.

        测试套件id

        :param suit_id: The suit_id of this ListSimBatchConfigsRequest.
        :type suit_id: int
        """
        self._suit_id = suit_id

    @property
    def triggerable(self):
        r"""Gets the triggerable of this ListSimBatchConfigsRequest.

        是否可通过流水线功能触发

        :return: The triggerable of this ListSimBatchConfigsRequest.
        :rtype: bool
        """
        return self._triggerable

    @triggerable.setter
    def triggerable(self, triggerable):
        r"""Sets the triggerable of this ListSimBatchConfigsRequest.

        是否可通过流水线功能触发

        :param triggerable: The triggerable of this ListSimBatchConfigsRequest.
        :type triggerable: bool
        """
        self._triggerable = triggerable

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
        if not isinstance(other, ListSimBatchConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
