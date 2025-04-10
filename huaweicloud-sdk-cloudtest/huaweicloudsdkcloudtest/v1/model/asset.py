# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Asset:

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
        'project_id': 'str',
        'create_time': 'datetime',
        'creator_name': 'str',
        'creator_num': 'str',
        'update_name': 'str',
        'update_num': 'str',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'creator_num': 'creator_num',
        'update_name': 'update_name',
        'update_num': 'update_num',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, project_id=None, create_time=None, creator_name=None, creator_num=None, update_name=None, update_num=None, update_time=None):
        r"""Asset

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param project_id: 
        :type project_id: str
        :param create_time: 
        :type create_time: datetime
        :param creator_name: 
        :type creator_name: str
        :param creator_num: 
        :type creator_num: str
        :param update_name: 
        :type update_name: str
        :param update_num: 
        :type update_num: str
        :param update_time: 
        :type update_time: datetime
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._create_time = None
        self._creator_name = None
        self._creator_num = None
        self._update_name = None
        self._update_num = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_num is not None:
            self.creator_num = creator_num
        if update_name is not None:
            self.update_name = update_name
        if update_num is not None:
            self.update_num = update_num
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this Asset.

        :return: The id of this Asset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Asset.

        :param id: The id of this Asset.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Asset.

        :return: The name of this Asset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Asset.

        :param name: The name of this Asset.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this Asset.

        :return: The project_id of this Asset.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Asset.

        :param project_id: The project_id of this Asset.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this Asset.

        :return: The create_time of this Asset.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Asset.

        :param create_time: The create_time of this Asset.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this Asset.

        :return: The creator_name of this Asset.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this Asset.

        :param creator_name: The creator_name of this Asset.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_num(self):
        r"""Gets the creator_num of this Asset.

        :return: The creator_num of this Asset.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this Asset.

        :param creator_num: The creator_num of this Asset.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def update_name(self):
        r"""Gets the update_name of this Asset.

        :return: The update_name of this Asset.
        :rtype: str
        """
        return self._update_name

    @update_name.setter
    def update_name(self, update_name):
        r"""Sets the update_name of this Asset.

        :param update_name: The update_name of this Asset.
        :type update_name: str
        """
        self._update_name = update_name

    @property
    def update_num(self):
        r"""Gets the update_num of this Asset.

        :return: The update_num of this Asset.
        :rtype: str
        """
        return self._update_num

    @update_num.setter
    def update_num(self, update_num):
        r"""Sets the update_num of this Asset.

        :param update_num: The update_num of this Asset.
        :type update_num: str
        """
        self._update_num = update_num

    @property
    def update_time(self):
        r"""Gets the update_time of this Asset.

        :return: The update_time of this Asset.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Asset.

        :param update_time: The update_time of this Asset.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, Asset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
