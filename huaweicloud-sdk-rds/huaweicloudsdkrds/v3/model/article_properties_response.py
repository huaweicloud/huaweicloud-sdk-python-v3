# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArticlePropertiesResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination_object_name': 'str',
        'destination_object_owner': 'str',
        'insert_delivery_format': 'str',
        'insert_stored_procedure': 'str',
        'update_delivery_format': 'str',
        'update_stored_procedure': 'str',
        'delete_delivery_format': 'str',
        'delete_stored_procedure': 'str'
    }

    attribute_map = {
        'destination_object_name': 'destination_object_name',
        'destination_object_owner': 'destination_object_owner',
        'insert_delivery_format': 'insert_delivery_format',
        'insert_stored_procedure': 'insert_stored_procedure',
        'update_delivery_format': 'update_delivery_format',
        'update_stored_procedure': 'update_stored_procedure',
        'delete_delivery_format': 'delete_delivery_format',
        'delete_stored_procedure': 'delete_stored_procedure'
    }

    def __init__(self, destination_object_name=None, destination_object_owner=None, insert_delivery_format=None, insert_stored_procedure=None, update_delivery_format=None, update_stored_procedure=None, delete_delivery_format=None, delete_stored_procedure=None):
        r"""ArticlePropertiesResponse

        The model defined in huaweicloud sdk

        :param destination_object_name: 目标对象名称。
        :type destination_object_name: str
        :param destination_object_owner: 目标对象命名空间。
        :type destination_object_owner: str
        :param insert_delivery_format: 插入交付格式。
        :type insert_delivery_format: str
        :param insert_stored_procedure: 插入存储过程。插入交付格式填call_procedure时该项必填。
        :type insert_stored_procedure: str
        :param update_delivery_format: 更新交付格式。
        :type update_delivery_format: str
        :param update_stored_procedure: 更新存储过程。更新交付格式填(m/x/s)call_procedure时该项必填。
        :type update_stored_procedure: str
        :param delete_delivery_format: 删除交付格式。
        :type delete_delivery_format: str
        :param delete_stored_procedure: 删除存储过程。删除交付格式填(x)call_procedure时该项必填。
        :type delete_stored_procedure: str
        """
        
        

        self._destination_object_name = None
        self._destination_object_owner = None
        self._insert_delivery_format = None
        self._insert_stored_procedure = None
        self._update_delivery_format = None
        self._update_stored_procedure = None
        self._delete_delivery_format = None
        self._delete_stored_procedure = None
        self.discriminator = None

        if destination_object_name is not None:
            self.destination_object_name = destination_object_name
        if destination_object_owner is not None:
            self.destination_object_owner = destination_object_owner
        if insert_delivery_format is not None:
            self.insert_delivery_format = insert_delivery_format
        if insert_stored_procedure is not None:
            self.insert_stored_procedure = insert_stored_procedure
        if update_delivery_format is not None:
            self.update_delivery_format = update_delivery_format
        if update_stored_procedure is not None:
            self.update_stored_procedure = update_stored_procedure
        if delete_delivery_format is not None:
            self.delete_delivery_format = delete_delivery_format
        if delete_stored_procedure is not None:
            self.delete_stored_procedure = delete_stored_procedure

    @property
    def destination_object_name(self):
        r"""Gets the destination_object_name of this ArticlePropertiesResponse.

        目标对象名称。

        :return: The destination_object_name of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._destination_object_name

    @destination_object_name.setter
    def destination_object_name(self, destination_object_name):
        r"""Sets the destination_object_name of this ArticlePropertiesResponse.

        目标对象名称。

        :param destination_object_name: The destination_object_name of this ArticlePropertiesResponse.
        :type destination_object_name: str
        """
        self._destination_object_name = destination_object_name

    @property
    def destination_object_owner(self):
        r"""Gets the destination_object_owner of this ArticlePropertiesResponse.

        目标对象命名空间。

        :return: The destination_object_owner of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._destination_object_owner

    @destination_object_owner.setter
    def destination_object_owner(self, destination_object_owner):
        r"""Sets the destination_object_owner of this ArticlePropertiesResponse.

        目标对象命名空间。

        :param destination_object_owner: The destination_object_owner of this ArticlePropertiesResponse.
        :type destination_object_owner: str
        """
        self._destination_object_owner = destination_object_owner

    @property
    def insert_delivery_format(self):
        r"""Gets the insert_delivery_format of this ArticlePropertiesResponse.

        插入交付格式。

        :return: The insert_delivery_format of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._insert_delivery_format

    @insert_delivery_format.setter
    def insert_delivery_format(self, insert_delivery_format):
        r"""Sets the insert_delivery_format of this ArticlePropertiesResponse.

        插入交付格式。

        :param insert_delivery_format: The insert_delivery_format of this ArticlePropertiesResponse.
        :type insert_delivery_format: str
        """
        self._insert_delivery_format = insert_delivery_format

    @property
    def insert_stored_procedure(self):
        r"""Gets the insert_stored_procedure of this ArticlePropertiesResponse.

        插入存储过程。插入交付格式填call_procedure时该项必填。

        :return: The insert_stored_procedure of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._insert_stored_procedure

    @insert_stored_procedure.setter
    def insert_stored_procedure(self, insert_stored_procedure):
        r"""Sets the insert_stored_procedure of this ArticlePropertiesResponse.

        插入存储过程。插入交付格式填call_procedure时该项必填。

        :param insert_stored_procedure: The insert_stored_procedure of this ArticlePropertiesResponse.
        :type insert_stored_procedure: str
        """
        self._insert_stored_procedure = insert_stored_procedure

    @property
    def update_delivery_format(self):
        r"""Gets the update_delivery_format of this ArticlePropertiesResponse.

        更新交付格式。

        :return: The update_delivery_format of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._update_delivery_format

    @update_delivery_format.setter
    def update_delivery_format(self, update_delivery_format):
        r"""Sets the update_delivery_format of this ArticlePropertiesResponse.

        更新交付格式。

        :param update_delivery_format: The update_delivery_format of this ArticlePropertiesResponse.
        :type update_delivery_format: str
        """
        self._update_delivery_format = update_delivery_format

    @property
    def update_stored_procedure(self):
        r"""Gets the update_stored_procedure of this ArticlePropertiesResponse.

        更新存储过程。更新交付格式填(m/x/s)call_procedure时该项必填。

        :return: The update_stored_procedure of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._update_stored_procedure

    @update_stored_procedure.setter
    def update_stored_procedure(self, update_stored_procedure):
        r"""Sets the update_stored_procedure of this ArticlePropertiesResponse.

        更新存储过程。更新交付格式填(m/x/s)call_procedure时该项必填。

        :param update_stored_procedure: The update_stored_procedure of this ArticlePropertiesResponse.
        :type update_stored_procedure: str
        """
        self._update_stored_procedure = update_stored_procedure

    @property
    def delete_delivery_format(self):
        r"""Gets the delete_delivery_format of this ArticlePropertiesResponse.

        删除交付格式。

        :return: The delete_delivery_format of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._delete_delivery_format

    @delete_delivery_format.setter
    def delete_delivery_format(self, delete_delivery_format):
        r"""Sets the delete_delivery_format of this ArticlePropertiesResponse.

        删除交付格式。

        :param delete_delivery_format: The delete_delivery_format of this ArticlePropertiesResponse.
        :type delete_delivery_format: str
        """
        self._delete_delivery_format = delete_delivery_format

    @property
    def delete_stored_procedure(self):
        r"""Gets the delete_stored_procedure of this ArticlePropertiesResponse.

        删除存储过程。删除交付格式填(x)call_procedure时该项必填。

        :return: The delete_stored_procedure of this ArticlePropertiesResponse.
        :rtype: str
        """
        return self._delete_stored_procedure

    @delete_stored_procedure.setter
    def delete_stored_procedure(self, delete_stored_procedure):
        r"""Sets the delete_stored_procedure of this ArticlePropertiesResponse.

        删除存储过程。删除交付格式填(x)call_procedure时该项必填。

        :param delete_stored_procedure: The delete_stored_procedure of this ArticlePropertiesResponse.
        :type delete_stored_procedure: str
        """
        self._delete_stored_procedure = delete_stored_procedure

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
        if not isinstance(other, ArticlePropertiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
