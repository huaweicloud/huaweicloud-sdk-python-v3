# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDdsConnectionStatRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'cur_page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'cur_page': 'cur_page',
        'per_page': 'per_page'
    }

    def __init__(self, instance_id=None, node_id=None, cur_page=None, per_page=None):
        r"""ShowDdsConnectionStatRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param node_id: 
        :type node_id: str
        :param cur_page: 
        :type cur_page: int
        :param per_page: 
        :type per_page: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._cur_page = None
        self._per_page = None
        self.discriminator = None

        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDdsConnectionStatRequest.

        实例ID

        :return: The instance_id of this ShowDdsConnectionStatRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDdsConnectionStatRequest.

        实例ID

        :param instance_id: The instance_id of this ShowDdsConnectionStatRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowDdsConnectionStatRequest.

        :return: The node_id of this ShowDdsConnectionStatRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowDdsConnectionStatRequest.

        :param node_id: The node_id of this ShowDdsConnectionStatRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ShowDdsConnectionStatRequest.

        :return: The cur_page of this ShowDdsConnectionStatRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ShowDdsConnectionStatRequest.

        :param cur_page: The cur_page of this ShowDdsConnectionStatRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ShowDdsConnectionStatRequest.

        :return: The per_page of this ShowDdsConnectionStatRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ShowDdsConnectionStatRequest.

        :param per_page: The per_page of this ShowDdsConnectionStatRequest.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ShowDdsConnectionStatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
