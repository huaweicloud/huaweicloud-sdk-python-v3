# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApplicationResponse(SdkResponse):

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
        'name': 'str',
        'creator': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'description': 'str',
        'labels': 'list[EnvironmentViewLabels]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'creator': 'creator',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description',
        'labels': 'labels'
    }

    def __init__(self, id=None, name=None, creator=None, project_id=None, enterprise_project_id=None, create_time=None, update_time=None, description=None, labels=None):
        r"""CreateApplicationResponse

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param creator: 
        :type creator: str
        :param project_id: 
        :type project_id: str
        :param enterprise_project_id: 
        :type enterprise_project_id: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        :param description: 
        :type description: str
        :param labels: 
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentViewLabels`]
        """
        
        super(CreateApplicationResponse, self).__init__()

        self._id = None
        self._name = None
        self._creator = None
        self._project_id = None
        self._enterprise_project_id = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self._labels = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if creator is not None:
            self.creator = creator
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels

    @property
    def id(self):
        r"""Gets the id of this CreateApplicationResponse.

        :return: The id of this CreateApplicationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateApplicationResponse.

        :param id: The id of this CreateApplicationResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateApplicationResponse.

        :return: The name of this CreateApplicationResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateApplicationResponse.

        :param name: The name of this CreateApplicationResponse.
        :type name: str
        """
        self._name = name

    @property
    def creator(self):
        r"""Gets the creator of this CreateApplicationResponse.

        :return: The creator of this CreateApplicationResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CreateApplicationResponse.

        :param creator: The creator of this CreateApplicationResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateApplicationResponse.

        :return: The project_id of this CreateApplicationResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateApplicationResponse.

        :param project_id: The project_id of this CreateApplicationResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateApplicationResponse.

        :return: The enterprise_project_id of this CreateApplicationResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateApplicationResponse.

        :param enterprise_project_id: The enterprise_project_id of this CreateApplicationResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateApplicationResponse.

        创建时间。

        :return: The create_time of this CreateApplicationResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateApplicationResponse.

        创建时间。

        :param create_time: The create_time of this CreateApplicationResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateApplicationResponse.

        修改时间。

        :return: The update_time of this CreateApplicationResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateApplicationResponse.

        修改时间。

        :param update_time: The update_time of this CreateApplicationResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this CreateApplicationResponse.

        :return: The description of this CreateApplicationResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateApplicationResponse.

        :param description: The description of this CreateApplicationResponse.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this CreateApplicationResponse.

        :return: The labels of this CreateApplicationResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentViewLabels`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateApplicationResponse.

        :param labels: The labels of this CreateApplicationResponse.
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.EnvironmentViewLabels`]
        """
        self._labels = labels

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
        if not isinstance(other, CreateApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
