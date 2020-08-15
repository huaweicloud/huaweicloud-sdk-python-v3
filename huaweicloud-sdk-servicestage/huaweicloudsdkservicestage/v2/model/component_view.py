# coding: utf-8

import pprint
import re

import six





class ComponentView:


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
        'application_id': 'str',
        'name': 'str',
        'runtime': 'RuntimeType',
        'category': 'ComponentCategory',
        'sub_category': 'ComponentSubCategory',
        'description': 'str',
        'status': 'int',
        'source': 'SourceObject',
        'creator': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'application_id': 'application_id',
        'name': 'name',
        'runtime': 'runtime',
        'category': 'category',
        'sub_category': 'sub_category',
        'description': 'description',
        'status': 'status',
        'source': 'source',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, application_id=None, name=None, runtime=None, category=None, sub_category=None, description=None, status=None, source=None, creator=None, create_time=None, update_time=None):
        """ComponentView - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._application_id = None
        self._name = None
        self._runtime = None
        self._category = None
        self._sub_category = None
        self._description = None
        self._status = None
        self._source = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application_id is not None:
            self.application_id = application_id
        if name is not None:
            self.name = name
        if runtime is not None:
            self.runtime = runtime
        if category is not None:
            self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if source is not None:
            self.source = source
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ComponentView.

        组件ID。

        :return: The id of this ComponentView.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentView.

        组件ID。

        :param id: The id of this ComponentView.
        :type: str
        """
        self._id = id

    @property
    def application_id(self):
        """Gets the application_id of this ComponentView.

        应用ID。

        :return: The application_id of this ComponentView.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ComponentView.

        应用ID。

        :param application_id: The application_id of this ComponentView.
        :type: str
        """
        self._application_id = application_id

    @property
    def name(self):
        """Gets the name of this ComponentView.

        应用组件名称。

        :return: The name of this ComponentView.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentView.

        应用组件名称。

        :param name: The name of this ComponentView.
        :type: str
        """
        self._name = name

    @property
    def runtime(self):
        """Gets the runtime of this ComponentView.


        :return: The runtime of this ComponentView.
        :rtype: RuntimeType
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ComponentView.


        :param runtime: The runtime of this ComponentView.
        :type: RuntimeType
        """
        self._runtime = runtime

    @property
    def category(self):
        """Gets the category of this ComponentView.


        :return: The category of this ComponentView.
        :rtype: ComponentCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ComponentView.


        :param category: The category of this ComponentView.
        :type: ComponentCategory
        """
        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this ComponentView.


        :return: The sub_category of this ComponentView.
        :rtype: ComponentSubCategory
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this ComponentView.


        :param sub_category: The sub_category of this ComponentView.
        :type: ComponentSubCategory
        """
        self._sub_category = sub_category

    @property
    def description(self):
        """Gets the description of this ComponentView.

        组件描述。

        :return: The description of this ComponentView.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComponentView.

        组件描述。

        :param description: The description of this ComponentView.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ComponentView.

        取值0或1。  0：表示正常状态。  1：表示正在删除。 

        :return: The status of this ComponentView.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComponentView.

        取值0或1。  0：表示正常状态。  1：表示正在删除。 

        :param status: The status of this ComponentView.
        :type: int
        """
        self._status = status

    @property
    def source(self):
        """Gets the source of this ComponentView.


        :return: The source of this ComponentView.
        :rtype: SourceObject
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComponentView.


        :param source: The source of this ComponentView.
        :type: SourceObject
        """
        self._source = source

    @property
    def creator(self):
        """Gets the creator of this ComponentView.

        创建人。

        :return: The creator of this ComponentView.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ComponentView.

        创建人。

        :param creator: The creator of this ComponentView.
        :type: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this ComponentView.

        创建时间。

        :return: The create_time of this ComponentView.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ComponentView.

        创建时间。

        :param create_time: The create_time of this ComponentView.
        :type: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ComponentView.

        修改时间。

        :return: The update_time of this ComponentView.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ComponentView.

        修改时间。

        :param update_time: The update_time of this ComponentView.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComponentView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
