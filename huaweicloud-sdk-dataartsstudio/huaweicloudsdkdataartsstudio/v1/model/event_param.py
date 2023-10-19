# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'guid': 'str',
        'type_name': 'str',
        'model_id': 'str',
        'property_name': 'str',
        'property_value': 'str',
        'query': 'str',
        'filter': 'DataMapFilterCriteria',
        'guid_list': 'list[str]',
        'trace_id': 'str',
        'source_trace_id': 'str',
        'metadata_type_name': 'str',
        'super_type_names': 'str',
        'workspace_ids': 'list[str]'
    }

    attribute_map = {
        'guid': 'guid',
        'type_name': 'type_name',
        'model_id': 'model_id',
        'property_name': 'property_name',
        'property_value': 'property_value',
        'query': 'query',
        'filter': 'filter',
        'guid_list': 'guid_list',
        'trace_id': 'trace_id',
        'source_trace_id': 'source_trace_id',
        'metadata_type_name': 'metadata_type_name',
        'super_type_names': 'super_type_names',
        'workspace_ids': 'workspace_ids'
    }

    def __init__(self, guid=None, type_name=None, model_id=None, property_name=None, property_value=None, query=None, filter=None, guid_list=None, trace_id=None, source_trace_id=None, metadata_type_name=None, super_type_names=None, workspace_ids=None):
        """EventParam

        The model defined in huaweicloud sdk

        :param guid: 
        :type guid: str
        :param type_name: 资产类型
        :type type_name: str
        :param model_id: 
        :type model_id: str
        :param property_name: 
        :type property_name: str
        :param property_value: 
        :type property_value: str
        :param query: 搜索框输入
        :type query: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`
        :param guid_list: 
        :type guid_list: list[str]
        :param trace_id: 
        :type trace_id: str
        :param source_trace_id: 
        :type source_trace_id: str
        :param metadata_type_name: 
        :type metadata_type_name: str
        :param super_type_names: 
        :type super_type_names: str
        :param workspace_ids: 
        :type workspace_ids: list[str]
        """
        
        

        self._guid = None
        self._type_name = None
        self._model_id = None
        self._property_name = None
        self._property_value = None
        self._query = None
        self._filter = None
        self._guid_list = None
        self._trace_id = None
        self._source_trace_id = None
        self._metadata_type_name = None
        self._super_type_names = None
        self._workspace_ids = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if type_name is not None:
            self.type_name = type_name
        if model_id is not None:
            self.model_id = model_id
        if property_name is not None:
            self.property_name = property_name
        if property_value is not None:
            self.property_value = property_value
        if query is not None:
            self.query = query
        if filter is not None:
            self.filter = filter
        if guid_list is not None:
            self.guid_list = guid_list
        if trace_id is not None:
            self.trace_id = trace_id
        if source_trace_id is not None:
            self.source_trace_id = source_trace_id
        if metadata_type_name is not None:
            self.metadata_type_name = metadata_type_name
        if super_type_names is not None:
            self.super_type_names = super_type_names
        if workspace_ids is not None:
            self.workspace_ids = workspace_ids

    @property
    def guid(self):
        """Gets the guid of this EventParam.

        :return: The guid of this EventParam.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this EventParam.

        :param guid: The guid of this EventParam.
        :type guid: str
        """
        self._guid = guid

    @property
    def type_name(self):
        """Gets the type_name of this EventParam.

        资产类型

        :return: The type_name of this EventParam.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this EventParam.

        资产类型

        :param type_name: The type_name of this EventParam.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def model_id(self):
        """Gets the model_id of this EventParam.

        :return: The model_id of this EventParam.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this EventParam.

        :param model_id: The model_id of this EventParam.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def property_name(self):
        """Gets the property_name of this EventParam.

        :return: The property_name of this EventParam.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this EventParam.

        :param property_name: The property_name of this EventParam.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def property_value(self):
        """Gets the property_value of this EventParam.

        :return: The property_value of this EventParam.
        :rtype: str
        """
        return self._property_value

    @property_value.setter
    def property_value(self, property_value):
        """Sets the property_value of this EventParam.

        :param property_value: The property_value of this EventParam.
        :type property_value: str
        """
        self._property_value = property_value

    @property
    def query(self):
        """Gets the query of this EventParam.

        搜索框输入

        :return: The query of this EventParam.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this EventParam.

        搜索框输入

        :param query: The query of this EventParam.
        :type query: str
        """
        self._query = query

    @property
    def filter(self):
        """Gets the filter of this EventParam.

        :return: The filter of this EventParam.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this EventParam.

        :param filter: The filter of this EventParam.
        :type filter: :class:`huaweicloudsdkdataartsstudio.v1.DataMapFilterCriteria`
        """
        self._filter = filter

    @property
    def guid_list(self):
        """Gets the guid_list of this EventParam.

        :return: The guid_list of this EventParam.
        :rtype: list[str]
        """
        return self._guid_list

    @guid_list.setter
    def guid_list(self, guid_list):
        """Sets the guid_list of this EventParam.

        :param guid_list: The guid_list of this EventParam.
        :type guid_list: list[str]
        """
        self._guid_list = guid_list

    @property
    def trace_id(self):
        """Gets the trace_id of this EventParam.

        :return: The trace_id of this EventParam.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this EventParam.

        :param trace_id: The trace_id of this EventParam.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def source_trace_id(self):
        """Gets the source_trace_id of this EventParam.

        :return: The source_trace_id of this EventParam.
        :rtype: str
        """
        return self._source_trace_id

    @source_trace_id.setter
    def source_trace_id(self, source_trace_id):
        """Sets the source_trace_id of this EventParam.

        :param source_trace_id: The source_trace_id of this EventParam.
        :type source_trace_id: str
        """
        self._source_trace_id = source_trace_id

    @property
    def metadata_type_name(self):
        """Gets the metadata_type_name of this EventParam.

        :return: The metadata_type_name of this EventParam.
        :rtype: str
        """
        return self._metadata_type_name

    @metadata_type_name.setter
    def metadata_type_name(self, metadata_type_name):
        """Sets the metadata_type_name of this EventParam.

        :param metadata_type_name: The metadata_type_name of this EventParam.
        :type metadata_type_name: str
        """
        self._metadata_type_name = metadata_type_name

    @property
    def super_type_names(self):
        """Gets the super_type_names of this EventParam.

        :return: The super_type_names of this EventParam.
        :rtype: str
        """
        return self._super_type_names

    @super_type_names.setter
    def super_type_names(self, super_type_names):
        """Sets the super_type_names of this EventParam.

        :param super_type_names: The super_type_names of this EventParam.
        :type super_type_names: str
        """
        self._super_type_names = super_type_names

    @property
    def workspace_ids(self):
        """Gets the workspace_ids of this EventParam.

        :return: The workspace_ids of this EventParam.
        :rtype: list[str]
        """
        return self._workspace_ids

    @workspace_ids.setter
    def workspace_ids(self, workspace_ids):
        """Sets the workspace_ids of this EventParam.

        :param workspace_ids: The workspace_ids of this EventParam.
        :type workspace_ids: list[str]
        """
        self._workspace_ids = workspace_ids

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
        if not isinstance(other, EventParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
