# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForkRepositoryBaseDto:

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
        'name': 'str',
        'archived': 'bool',
        'product_id': 'str',
        'product_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'archived': 'archived',
        'product_id': 'product_id',
        'product_name': 'product_name'
    }

    def __init__(self, id=None, name=None, archived=None, product_id=None, product_name=None):
        r"""ForkRepositoryBaseDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库ID。 **约束限制：** 不涉及。
        :type id: int
        :param name: **参数解释：** 仓库名称。 **约束限制：** 不涉及。
        :type name: str
        :param archived: **参数解释：** 是否归档。 **约束限制：** 不涉及。
        :type archived: bool
        :param product_id: **参数解释：** 产品ID。 **约束限制：** 不涉及。
        :type product_id: str
        :param product_name: **参数解释：** 产品名称。 **约束限制：** 不涉及。
        :type product_name: str
        """
        
        

        self._id = None
        self._name = None
        self._archived = None
        self._product_id = None
        self._product_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if archived is not None:
            self.archived = archived
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name

    @property
    def id(self):
        r"""Gets the id of this ForkRepositoryBaseDto.

        **参数解释：** 仓库ID。 **约束限制：** 不涉及。

        :return: The id of this ForkRepositoryBaseDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ForkRepositoryBaseDto.

        **参数解释：** 仓库ID。 **约束限制：** 不涉及。

        :param id: The id of this ForkRepositoryBaseDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ForkRepositoryBaseDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :return: The name of this ForkRepositoryBaseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ForkRepositoryBaseDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :param name: The name of this ForkRepositoryBaseDto.
        :type name: str
        """
        self._name = name

    @property
    def archived(self):
        r"""Gets the archived of this ForkRepositoryBaseDto.

        **参数解释：** 是否归档。 **约束限制：** 不涉及。

        :return: The archived of this ForkRepositoryBaseDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this ForkRepositoryBaseDto.

        **参数解释：** 是否归档。 **约束限制：** 不涉及。

        :param archived: The archived of this ForkRepositoryBaseDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def product_id(self):
        r"""Gets the product_id of this ForkRepositoryBaseDto.

        **参数解释：** 产品ID。 **约束限制：** 不涉及。

        :return: The product_id of this ForkRepositoryBaseDto.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ForkRepositoryBaseDto.

        **参数解释：** 产品ID。 **约束限制：** 不涉及。

        :param product_id: The product_id of this ForkRepositoryBaseDto.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this ForkRepositoryBaseDto.

        **参数解释：** 产品名称。 **约束限制：** 不涉及。

        :return: The product_name of this ForkRepositoryBaseDto.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this ForkRepositoryBaseDto.

        **参数解释：** 产品名称。 **约束限制：** 不涉及。

        :param product_name: The product_name of this ForkRepositoryBaseDto.
        :type product_name: str
        """
        self._product_name = product_name

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
        if not isinstance(other, ForkRepositoryBaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
