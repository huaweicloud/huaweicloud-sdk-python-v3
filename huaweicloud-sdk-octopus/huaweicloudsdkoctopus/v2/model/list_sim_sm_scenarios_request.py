# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimSmScenariosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exclude_group': 'int',
        'file': 'str',
        'gen_scenario': 'str',
        'group': 'list[int]',
        'id': 'int',
        'label': 'float',
        'map': 'int',
        'name': 'str',
        'ordering': 'str',
        'offset': 'int',
        'limit': 'int',
        'search': 'str',
        'simulator': 'str',
        'source': 'str',
        'status': 'int',
        'user_name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'exclude_group': 'exclude_group',
        'file': 'file',
        'gen_scenario': 'gen_scenario',
        'group': 'group',
        'id': 'id',
        'label': 'label',
        'map': 'map',
        'name': 'name',
        'ordering': 'ordering',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search',
        'simulator': 'simulator',
        'source': 'source',
        'status': 'status',
        'user_name': 'user_name',
        'version': 'version'
    }

    def __init__(self, exclude_group=None, file=None, gen_scenario=None, group=None, id=None, label=None, map=None, name=None, ordering=None, offset=None, limit=None, search=None, simulator=None, source=None, status=None, user_name=None, version=None):
        r"""ListSimSmScenariosRequest

        The model defined in huaweicloud sdk

        :param exclude_group: 
        :type exclude_group: int
        :param file: 
        :type file: str
        :param gen_scenario: 
        :type gen_scenario: str
        :param group: 
        :type group: list[int]
        :param id: 
        :type id: int
        :param label: label
        :type label: float
        :param map: 
        :type map: int
        :param name: 
        :type name: str
        :param ordering: Which field to use when ordering the results.
        :type ordering: str
        :param offset: A page number within the paginated result set.
        :type offset: int
        :param limit: Number of results to return per page.
        :type limit: int
        :param search: A search term.
        :type search: str
        :param simulator: 仿真器名称,取值范围:A,B,C,D,E
        :type simulator: str
        :param source: Choices: generalization, road, upload
        :type source: str
        :param status: * &#x60;0&#x60; - Released * &#x60;1&#x60; - Available * &#x60;10&#x60; - Initial * &#x60;11&#x60; - Unavailable * &#x60;12&#x60; - Releasing * &#x60;100&#x60; - Deprecated
        :type status: int
        :param user_name: 
        :type user_name: str
        :param version: * &#x60;vtd&#x60; - vtd * &#x60;v0.9.1&#x60; - v0.9.1 * &#x60;v1.0.0&#x60; - v1.0.0 * &#x60;v1.1.0&#x60; - v1.1.0 * &#x60;v1.1.1&#x60; - v1.1.1
        :type version: str
        """
        
        

        self._exclude_group = None
        self._file = None
        self._gen_scenario = None
        self._group = None
        self._id = None
        self._label = None
        self._map = None
        self._name = None
        self._ordering = None
        self._offset = None
        self._limit = None
        self._search = None
        self._simulator = None
        self._source = None
        self._status = None
        self._user_name = None
        self._version = None
        self.discriminator = None

        if exclude_group is not None:
            self.exclude_group = exclude_group
        if file is not None:
            self.file = file
        if gen_scenario is not None:
            self.gen_scenario = gen_scenario
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if map is not None:
            self.map = map
        if name is not None:
            self.name = name
        if ordering is not None:
            self.ordering = ordering
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search
        if simulator is not None:
            self.simulator = simulator
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status
        if user_name is not None:
            self.user_name = user_name
        if version is not None:
            self.version = version

    @property
    def exclude_group(self):
        r"""Gets the exclude_group of this ListSimSmScenariosRequest.

        :return: The exclude_group of this ListSimSmScenariosRequest.
        :rtype: int
        """
        return self._exclude_group

    @exclude_group.setter
    def exclude_group(self, exclude_group):
        r"""Sets the exclude_group of this ListSimSmScenariosRequest.

        :param exclude_group: The exclude_group of this ListSimSmScenariosRequest.
        :type exclude_group: int
        """
        self._exclude_group = exclude_group

    @property
    def file(self):
        r"""Gets the file of this ListSimSmScenariosRequest.

        :return: The file of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ListSimSmScenariosRequest.

        :param file: The file of this ListSimSmScenariosRequest.
        :type file: str
        """
        self._file = file

    @property
    def gen_scenario(self):
        r"""Gets the gen_scenario of this ListSimSmScenariosRequest.

        :return: The gen_scenario of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._gen_scenario

    @gen_scenario.setter
    def gen_scenario(self, gen_scenario):
        r"""Sets the gen_scenario of this ListSimSmScenariosRequest.

        :param gen_scenario: The gen_scenario of this ListSimSmScenariosRequest.
        :type gen_scenario: str
        """
        self._gen_scenario = gen_scenario

    @property
    def group(self):
        r"""Gets the group of this ListSimSmScenariosRequest.

        :return: The group of this ListSimSmScenariosRequest.
        :rtype: list[int]
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListSimSmScenariosRequest.

        :param group: The group of this ListSimSmScenariosRequest.
        :type group: list[int]
        """
        self._group = group

    @property
    def id(self):
        r"""Gets the id of this ListSimSmScenariosRequest.

        :return: The id of this ListSimSmScenariosRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSimSmScenariosRequest.

        :param id: The id of this ListSimSmScenariosRequest.
        :type id: int
        """
        self._id = id

    @property
    def label(self):
        r"""Gets the label of this ListSimSmScenariosRequest.

        label

        :return: The label of this ListSimSmScenariosRequest.
        :rtype: float
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ListSimSmScenariosRequest.

        label

        :param label: The label of this ListSimSmScenariosRequest.
        :type label: float
        """
        self._label = label

    @property
    def map(self):
        r"""Gets the map of this ListSimSmScenariosRequest.

        :return: The map of this ListSimSmScenariosRequest.
        :rtype: int
        """
        return self._map

    @map.setter
    def map(self, map):
        r"""Sets the map of this ListSimSmScenariosRequest.

        :param map: The map of this ListSimSmScenariosRequest.
        :type map: int
        """
        self._map = map

    @property
    def name(self):
        r"""Gets the name of this ListSimSmScenariosRequest.

        :return: The name of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSimSmScenariosRequest.

        :param name: The name of this ListSimSmScenariosRequest.
        :type name: str
        """
        self._name = name

    @property
    def ordering(self):
        r"""Gets the ordering of this ListSimSmScenariosRequest.

        Which field to use when ordering the results.

        :return: The ordering of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._ordering

    @ordering.setter
    def ordering(self, ordering):
        r"""Sets the ordering of this ListSimSmScenariosRequest.

        Which field to use when ordering the results.

        :param ordering: The ordering of this ListSimSmScenariosRequest.
        :type ordering: str
        """
        self._ordering = ordering

    @property
    def offset(self):
        r"""Gets the offset of this ListSimSmScenariosRequest.

        A page number within the paginated result set.

        :return: The offset of this ListSimSmScenariosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimSmScenariosRequest.

        A page number within the paginated result set.

        :param offset: The offset of this ListSimSmScenariosRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSimSmScenariosRequest.

        Number of results to return per page.

        :return: The limit of this ListSimSmScenariosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimSmScenariosRequest.

        Number of results to return per page.

        :param limit: The limit of this ListSimSmScenariosRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListSimSmScenariosRequest.

        A search term.

        :return: The search of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListSimSmScenariosRequest.

        A search term.

        :param search: The search of this ListSimSmScenariosRequest.
        :type search: str
        """
        self._search = search

    @property
    def simulator(self):
        r"""Gets the simulator of this ListSimSmScenariosRequest.

        仿真器名称,取值范围:A,B,C,D,E

        :return: The simulator of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._simulator

    @simulator.setter
    def simulator(self, simulator):
        r"""Sets the simulator of this ListSimSmScenariosRequest.

        仿真器名称,取值范围:A,B,C,D,E

        :param simulator: The simulator of this ListSimSmScenariosRequest.
        :type simulator: str
        """
        self._simulator = simulator

    @property
    def source(self):
        r"""Gets the source of this ListSimSmScenariosRequest.

        Choices: generalization, road, upload

        :return: The source of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ListSimSmScenariosRequest.

        Choices: generalization, road, upload

        :param source: The source of this ListSimSmScenariosRequest.
        :type source: str
        """
        self._source = source

    @property
    def status(self):
        r"""Gets the status of this ListSimSmScenariosRequest.

        * `0` - Released * `1` - Available * `10` - Initial * `11` - Unavailable * `12` - Releasing * `100` - Deprecated

        :return: The status of this ListSimSmScenariosRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSimSmScenariosRequest.

        * `0` - Released * `1` - Available * `10` - Initial * `11` - Unavailable * `12` - Releasing * `100` - Deprecated

        :param status: The status of this ListSimSmScenariosRequest.
        :type status: int
        """
        self._status = status

    @property
    def user_name(self):
        r"""Gets the user_name of this ListSimSmScenariosRequest.

        :return: The user_name of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListSimSmScenariosRequest.

        :param user_name: The user_name of this ListSimSmScenariosRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def version(self):
        r"""Gets the version of this ListSimSmScenariosRequest.

        * `vtd` - vtd * `v0.9.1` - v0.9.1 * `v1.0.0` - v1.0.0 * `v1.1.0` - v1.1.0 * `v1.1.1` - v1.1.1

        :return: The version of this ListSimSmScenariosRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListSimSmScenariosRequest.

        * `vtd` - vtd * `v0.9.1` - v0.9.1 * `v1.0.0` - v1.0.0 * `v1.1.0` - v1.1.0 * `v1.1.1` - v1.1.1

        :param version: The version of this ListSimSmScenariosRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ListSimSmScenariosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
