# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTempRequestBody:

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
        'project_id': 'int',
        'name': 'str',
        'temp_type': 'int',
        'description': 'str',
        'for_loop_params': 'list[object]',
        'enable_pre': 'bool',
        'contents': 'list[TempContentInfo]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'temp_type': 'temp_type',
        'description': 'description',
        'for_loop_params': 'for_loop_params',
        'enable_pre': 'enable_pre',
        'contents': 'contents'
    }

    def __init__(self, id=None, project_id=None, name=None, temp_type=None, description=None, for_loop_params=None, enable_pre=None, contents=None):
        """UpdateTempRequestBody

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param project_id: project_id
        :type project_id: int
        :param name: name
        :type name: str
        :param temp_type: temp_type
        :type temp_type: int
        :param description: description
        :type description: str
        :param for_loop_params: for_loop_params
        :type for_loop_params: list[object]
        :param enable_pre: enable_pre
        :type enable_pre: bool
        :param contents: contents
        :type contents: list[:class:`huaweicloudsdkcpts.v1.TempContentInfo`]
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._temp_type = None
        self._description = None
        self._for_loop_params = None
        self._enable_pre = None
        self._contents = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.name = name
        if temp_type is not None:
            self.temp_type = temp_type
        if description is not None:
            self.description = description
        if for_loop_params is not None:
            self.for_loop_params = for_loop_params
        if enable_pre is not None:
            self.enable_pre = enable_pre
        if contents is not None:
            self.contents = contents

    @property
    def id(self):
        """Gets the id of this UpdateTempRequestBody.

        id

        :return: The id of this UpdateTempRequestBody.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateTempRequestBody.

        id

        :param id: The id of this UpdateTempRequestBody.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this UpdateTempRequestBody.

        project_id

        :return: The project_id of this UpdateTempRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateTempRequestBody.

        project_id

        :param project_id: The project_id of this UpdateTempRequestBody.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this UpdateTempRequestBody.

        name

        :return: The name of this UpdateTempRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTempRequestBody.

        name

        :param name: The name of this UpdateTempRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def temp_type(self):
        """Gets the temp_type of this UpdateTempRequestBody.

        temp_type

        :return: The temp_type of this UpdateTempRequestBody.
        :rtype: int
        """
        return self._temp_type

    @temp_type.setter
    def temp_type(self, temp_type):
        """Sets the temp_type of this UpdateTempRequestBody.

        temp_type

        :param temp_type: The temp_type of this UpdateTempRequestBody.
        :type temp_type: int
        """
        self._temp_type = temp_type

    @property
    def description(self):
        """Gets the description of this UpdateTempRequestBody.

        description

        :return: The description of this UpdateTempRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTempRequestBody.

        description

        :param description: The description of this UpdateTempRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def for_loop_params(self):
        """Gets the for_loop_params of this UpdateTempRequestBody.

        for_loop_params

        :return: The for_loop_params of this UpdateTempRequestBody.
        :rtype: list[object]
        """
        return self._for_loop_params

    @for_loop_params.setter
    def for_loop_params(self, for_loop_params):
        """Sets the for_loop_params of this UpdateTempRequestBody.

        for_loop_params

        :param for_loop_params: The for_loop_params of this UpdateTempRequestBody.
        :type for_loop_params: list[object]
        """
        self._for_loop_params = for_loop_params

    @property
    def enable_pre(self):
        """Gets the enable_pre of this UpdateTempRequestBody.

        enable_pre

        :return: The enable_pre of this UpdateTempRequestBody.
        :rtype: bool
        """
        return self._enable_pre

    @enable_pre.setter
    def enable_pre(self, enable_pre):
        """Sets the enable_pre of this UpdateTempRequestBody.

        enable_pre

        :param enable_pre: The enable_pre of this UpdateTempRequestBody.
        :type enable_pre: bool
        """
        self._enable_pre = enable_pre

    @property
    def contents(self):
        """Gets the contents of this UpdateTempRequestBody.

        contents

        :return: The contents of this UpdateTempRequestBody.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.TempContentInfo`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this UpdateTempRequestBody.

        contents

        :param contents: The contents of this UpdateTempRequestBody.
        :type contents: list[:class:`huaweicloudsdkcpts.v1.TempContentInfo`]
        """
        self._contents = contents

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
        if not isinstance(other, UpdateTempRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
