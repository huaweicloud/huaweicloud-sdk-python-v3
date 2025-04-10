# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRspResourceList:

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
        'type': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, type=None, domain_id=None, project_id=None, region_id=None, ep_id=None, ep_name=None, tags=None):
        r"""ShowAlertRspResourceList

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param name: The name, display only
        :type name: str
        :param type: The name, display only
        :type type: str
        :param domain_id: Id value
        :type domain_id: str
        :param project_id: Id value
        :type project_id: str
        :param region_id: Id value
        :type region_id: str
        :param ep_id: Id value
        :type ep_id: str
        :param ep_name: The name, display only
        :type ep_name: str
        :param tags: Id value
        :type tags: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._domain_id = None
        self._project_id = None
        self._region_id = None
        self._ep_id = None
        self._ep_name = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this ShowAlertRspResourceList.

        Id value

        :return: The id of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAlertRspResourceList.

        Id value

        :param id: The id of this ShowAlertRspResourceList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowAlertRspResourceList.

        The name, display only

        :return: The name of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAlertRspResourceList.

        The name, display only

        :param name: The name of this ShowAlertRspResourceList.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ShowAlertRspResourceList.

        The name, display only

        :return: The type of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAlertRspResourceList.

        The name, display only

        :param type: The type of this ShowAlertRspResourceList.
        :type type: str
        """
        self._type = type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowAlertRspResourceList.

        Id value

        :return: The domain_id of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowAlertRspResourceList.

        Id value

        :param domain_id: The domain_id of this ShowAlertRspResourceList.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAlertRspResourceList.

        Id value

        :return: The project_id of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAlertRspResourceList.

        Id value

        :param project_id: The project_id of this ShowAlertRspResourceList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowAlertRspResourceList.

        Id value

        :return: The region_id of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowAlertRspResourceList.

        Id value

        :param region_id: The region_id of this ShowAlertRspResourceList.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ShowAlertRspResourceList.

        Id value

        :return: The ep_id of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ShowAlertRspResourceList.

        Id value

        :param ep_id: The ep_id of this ShowAlertRspResourceList.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this ShowAlertRspResourceList.

        The name, display only

        :return: The ep_name of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this ShowAlertRspResourceList.

        The name, display only

        :param ep_name: The ep_name of this ShowAlertRspResourceList.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def tags(self):
        r"""Gets the tags of this ShowAlertRspResourceList.

        Id value

        :return: The tags of this ShowAlertRspResourceList.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowAlertRspResourceList.

        Id value

        :param tags: The tags of this ShowAlertRspResourceList.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ShowAlertRspResourceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
