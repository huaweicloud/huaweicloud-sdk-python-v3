# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DpeClassifyItemDetail:

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
        'classifier_id': 'str',
        'classifier_type_id': 'str',
        'mapping_id': 'str',
        'classifier_order': 'int',
        'expression': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'classifier_id': 'classifier_id',
        'classifier_type_id': 'classifier_type_id',
        'mapping_id': 'mapping_id',
        'classifier_order': 'classifier_order',
        'expression': 'expression',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, classifier_id=None, classifier_type_id=None, mapping_id=None, classifier_order=None, expression=None, create_time=None, update_time=None):
        r"""DpeClassifyItemDetail

        The model defined in huaweicloud sdk

        :param id: 映射id
        :type id: str
        :param classifier_id: 映射id
        :type classifier_id: str
        :param classifier_type_id: 映射id
        :type classifier_type_id: str
        :param mapping_id: 映射id
        :type mapping_id: str
        :param classifier_order: 分类优先级
        :type classifier_order: int
        :param expression: 表达式
        :type expression: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._id = None
        self._classifier_id = None
        self._classifier_type_id = None
        self._mapping_id = None
        self._classifier_order = None
        self._expression = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if classifier_id is not None:
            self.classifier_id = classifier_id
        if classifier_type_id is not None:
            self.classifier_type_id = classifier_type_id
        if mapping_id is not None:
            self.mapping_id = mapping_id
        if classifier_order is not None:
            self.classifier_order = classifier_order
        if expression is not None:
            self.expression = expression
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this DpeClassifyItemDetail.

        映射id

        :return: The id of this DpeClassifyItemDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DpeClassifyItemDetail.

        映射id

        :param id: The id of this DpeClassifyItemDetail.
        :type id: str
        """
        self._id = id

    @property
    def classifier_id(self):
        r"""Gets the classifier_id of this DpeClassifyItemDetail.

        映射id

        :return: The classifier_id of this DpeClassifyItemDetail.
        :rtype: str
        """
        return self._classifier_id

    @classifier_id.setter
    def classifier_id(self, classifier_id):
        r"""Sets the classifier_id of this DpeClassifyItemDetail.

        映射id

        :param classifier_id: The classifier_id of this DpeClassifyItemDetail.
        :type classifier_id: str
        """
        self._classifier_id = classifier_id

    @property
    def classifier_type_id(self):
        r"""Gets the classifier_type_id of this DpeClassifyItemDetail.

        映射id

        :return: The classifier_type_id of this DpeClassifyItemDetail.
        :rtype: str
        """
        return self._classifier_type_id

    @classifier_type_id.setter
    def classifier_type_id(self, classifier_type_id):
        r"""Sets the classifier_type_id of this DpeClassifyItemDetail.

        映射id

        :param classifier_type_id: The classifier_type_id of this DpeClassifyItemDetail.
        :type classifier_type_id: str
        """
        self._classifier_type_id = classifier_type_id

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this DpeClassifyItemDetail.

        映射id

        :return: The mapping_id of this DpeClassifyItemDetail.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this DpeClassifyItemDetail.

        映射id

        :param mapping_id: The mapping_id of this DpeClassifyItemDetail.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def classifier_order(self):
        r"""Gets the classifier_order of this DpeClassifyItemDetail.

        分类优先级

        :return: The classifier_order of this DpeClassifyItemDetail.
        :rtype: int
        """
        return self._classifier_order

    @classifier_order.setter
    def classifier_order(self, classifier_order):
        r"""Sets the classifier_order of this DpeClassifyItemDetail.

        分类优先级

        :param classifier_order: The classifier_order of this DpeClassifyItemDetail.
        :type classifier_order: int
        """
        self._classifier_order = classifier_order

    @property
    def expression(self):
        r"""Gets the expression of this DpeClassifyItemDetail.

        表达式

        :return: The expression of this DpeClassifyItemDetail.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this DpeClassifyItemDetail.

        表达式

        :param expression: The expression of this DpeClassifyItemDetail.
        :type expression: str
        """
        self._expression = expression

    @property
    def create_time(self):
        r"""Gets the create_time of this DpeClassifyItemDetail.

        创建时间

        :return: The create_time of this DpeClassifyItemDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DpeClassifyItemDetail.

        创建时间

        :param create_time: The create_time of this DpeClassifyItemDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DpeClassifyItemDetail.

        更新时间

        :return: The update_time of this DpeClassifyItemDetail.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DpeClassifyItemDetail.

        更新时间

        :param update_time: The update_time of this DpeClassifyItemDetail.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, DpeClassifyItemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
