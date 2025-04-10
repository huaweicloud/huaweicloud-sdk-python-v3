# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPublishDTO:

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
        'api_id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'api_status': 'str',
        'api_debug': 'str'
    }

    attribute_map = {
        'id': 'id',
        'api_id': 'api_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'api_status': 'api_status',
        'api_debug': 'api_debug'
    }

    def __init__(self, id=None, api_id=None, instance_id=None, instance_name=None, api_status=None, api_debug=None):
        r"""ApiPublishDTO

        The model defined in huaweicloud sdk

        :param id: 发布编号
        :type id: str
        :param api_id: api编号
        :type api_id: str
        :param instance_id: 集群编号
        :type instance_id: str
        :param instance_name: 集群名称
        :type instance_name: str
        :param api_status: api状态
        :type api_status: str
        :param api_debug: api调试状态
        :type api_debug: str
        """
        
        

        self._id = None
        self._api_id = None
        self._instance_id = None
        self._instance_name = None
        self._api_status = None
        self._api_debug = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if api_id is not None:
            self.api_id = api_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if api_status is not None:
            self.api_status = api_status
        if api_debug is not None:
            self.api_debug = api_debug

    @property
    def id(self):
        r"""Gets the id of this ApiPublishDTO.

        发布编号

        :return: The id of this ApiPublishDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApiPublishDTO.

        发布编号

        :param id: The id of this ApiPublishDTO.
        :type id: str
        """
        self._id = id

    @property
    def api_id(self):
        r"""Gets the api_id of this ApiPublishDTO.

        api编号

        :return: The api_id of this ApiPublishDTO.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this ApiPublishDTO.

        api编号

        :param api_id: The api_id of this ApiPublishDTO.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ApiPublishDTO.

        集群编号

        :return: The instance_id of this ApiPublishDTO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ApiPublishDTO.

        集群编号

        :param instance_id: The instance_id of this ApiPublishDTO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ApiPublishDTO.

        集群名称

        :return: The instance_name of this ApiPublishDTO.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ApiPublishDTO.

        集群名称

        :param instance_name: The instance_name of this ApiPublishDTO.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def api_status(self):
        r"""Gets the api_status of this ApiPublishDTO.

        api状态

        :return: The api_status of this ApiPublishDTO.
        :rtype: str
        """
        return self._api_status

    @api_status.setter
    def api_status(self, api_status):
        r"""Sets the api_status of this ApiPublishDTO.

        api状态

        :param api_status: The api_status of this ApiPublishDTO.
        :type api_status: str
        """
        self._api_status = api_status

    @property
    def api_debug(self):
        r"""Gets the api_debug of this ApiPublishDTO.

        api调试状态

        :return: The api_debug of this ApiPublishDTO.
        :rtype: str
        """
        return self._api_debug

    @api_debug.setter
    def api_debug(self, api_debug):
        r"""Sets the api_debug of this ApiPublishDTO.

        api调试状态

        :param api_debug: The api_debug of this ApiPublishDTO.
        :type api_debug: str
        """
        self._api_debug = api_debug

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
        if not isinstance(other, ApiPublishDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
