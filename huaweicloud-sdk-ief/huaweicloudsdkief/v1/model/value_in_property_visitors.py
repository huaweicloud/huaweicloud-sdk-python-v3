# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValueInPropertyVisitors:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'register_type': 'ValueInPropertyVisitorsRegisterType',
        'access_mode': 'ValueInPropertyVisitorsAccessMode',
        'register_index': 'ValueInPropertyVisitorsRegisterIndex',
        'register_num': 'ValueInPropertyVisitorsRegisterNum',
        'scale_index': 'ValueInPropertyVisitorsScaleIndex',
        'original_datatype': 'ValueInPropertyVisitorsOriginalDatatype',
        'expected_datatype': 'ValueInPropertyVisitorsExpectedDatatype',
        'is_registerswap': 'ValueInPropertyVisitorsIsRegisterswap',
        'is_swap': 'ValueInPropertyVisitorsIsSwap',
        'sample_interval': 'ValueInPropertyVisitorsSampleInterval',
        'data_min': 'ValueInPropertyVisitorsDataMin',
        'data_max': 'ValueInPropertyVisitorsDataMax',
        'node_id': 'ValueInPropertyVisitorsNodeId',
        'browse_name': 'ValueInPropertyVisitorsBrowseName'
    }

    attribute_map = {
        'register_type': 'register_type',
        'access_mode': 'access_mode',
        'register_index': 'register_index',
        'register_num': 'register_num',
        'scale_index': 'scale_index',
        'original_datatype': 'original_datatype',
        'expected_datatype': 'expected_datatype',
        'is_registerswap': 'is_registerswap',
        'is_swap': 'is_swap',
        'sample_interval': 'sample_interval',
        'data_min': 'data_min',
        'data_max': 'data_max',
        'node_id': 'node_id',
        'browse_name': 'browse_name'
    }

    def __init__(self, register_type=None, access_mode=None, register_index=None, register_num=None, scale_index=None, original_datatype=None, expected_datatype=None, is_registerswap=None, is_swap=None, sample_interval=None, data_min=None, data_max=None, node_id=None, browse_name=None):
        """ValueInPropertyVisitors - a model defined in huaweicloud sdk"""
        
        

        self._register_type = None
        self._access_mode = None
        self._register_index = None
        self._register_num = None
        self._scale_index = None
        self._original_datatype = None
        self._expected_datatype = None
        self._is_registerswap = None
        self._is_swap = None
        self._sample_interval = None
        self._data_min = None
        self._data_max = None
        self._node_id = None
        self._browse_name = None
        self.discriminator = None

        if register_type is not None:
            self.register_type = register_type
        if access_mode is not None:
            self.access_mode = access_mode
        if register_index is not None:
            self.register_index = register_index
        if register_num is not None:
            self.register_num = register_num
        if scale_index is not None:
            self.scale_index = scale_index
        if original_datatype is not None:
            self.original_datatype = original_datatype
        if expected_datatype is not None:
            self.expected_datatype = expected_datatype
        if is_registerswap is not None:
            self.is_registerswap = is_registerswap
        if is_swap is not None:
            self.is_swap = is_swap
        if sample_interval is not None:
            self.sample_interval = sample_interval
        if data_min is not None:
            self.data_min = data_min
        if data_max is not None:
            self.data_max = data_max
        if node_id is not None:
            self.node_id = node_id
        if browse_name is not None:
            self.browse_name = browse_name

    @property
    def register_type(self):
        """Gets the register_type of this ValueInPropertyVisitors.


        :return: The register_type of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsRegisterType
        """
        return self._register_type

    @register_type.setter
    def register_type(self, register_type):
        """Sets the register_type of this ValueInPropertyVisitors.


        :param register_type: The register_type of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsRegisterType
        """
        self._register_type = register_type

    @property
    def access_mode(self):
        """Gets the access_mode of this ValueInPropertyVisitors.


        :return: The access_mode of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsAccessMode
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this ValueInPropertyVisitors.


        :param access_mode: The access_mode of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsAccessMode
        """
        self._access_mode = access_mode

    @property
    def register_index(self):
        """Gets the register_index of this ValueInPropertyVisitors.


        :return: The register_index of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsRegisterIndex
        """
        return self._register_index

    @register_index.setter
    def register_index(self, register_index):
        """Sets the register_index of this ValueInPropertyVisitors.


        :param register_index: The register_index of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsRegisterIndex
        """
        self._register_index = register_index

    @property
    def register_num(self):
        """Gets the register_num of this ValueInPropertyVisitors.


        :return: The register_num of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsRegisterNum
        """
        return self._register_num

    @register_num.setter
    def register_num(self, register_num):
        """Sets the register_num of this ValueInPropertyVisitors.


        :param register_num: The register_num of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsRegisterNum
        """
        self._register_num = register_num

    @property
    def scale_index(self):
        """Gets the scale_index of this ValueInPropertyVisitors.


        :return: The scale_index of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsScaleIndex
        """
        return self._scale_index

    @scale_index.setter
    def scale_index(self, scale_index):
        """Sets the scale_index of this ValueInPropertyVisitors.


        :param scale_index: The scale_index of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsScaleIndex
        """
        self._scale_index = scale_index

    @property
    def original_datatype(self):
        """Gets the original_datatype of this ValueInPropertyVisitors.


        :return: The original_datatype of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsOriginalDatatype
        """
        return self._original_datatype

    @original_datatype.setter
    def original_datatype(self, original_datatype):
        """Sets the original_datatype of this ValueInPropertyVisitors.


        :param original_datatype: The original_datatype of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsOriginalDatatype
        """
        self._original_datatype = original_datatype

    @property
    def expected_datatype(self):
        """Gets the expected_datatype of this ValueInPropertyVisitors.


        :return: The expected_datatype of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsExpectedDatatype
        """
        return self._expected_datatype

    @expected_datatype.setter
    def expected_datatype(self, expected_datatype):
        """Sets the expected_datatype of this ValueInPropertyVisitors.


        :param expected_datatype: The expected_datatype of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsExpectedDatatype
        """
        self._expected_datatype = expected_datatype

    @property
    def is_registerswap(self):
        """Gets the is_registerswap of this ValueInPropertyVisitors.


        :return: The is_registerswap of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsIsRegisterswap
        """
        return self._is_registerswap

    @is_registerswap.setter
    def is_registerswap(self, is_registerswap):
        """Sets the is_registerswap of this ValueInPropertyVisitors.


        :param is_registerswap: The is_registerswap of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsIsRegisterswap
        """
        self._is_registerswap = is_registerswap

    @property
    def is_swap(self):
        """Gets the is_swap of this ValueInPropertyVisitors.


        :return: The is_swap of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsIsSwap
        """
        return self._is_swap

    @is_swap.setter
    def is_swap(self, is_swap):
        """Sets the is_swap of this ValueInPropertyVisitors.


        :param is_swap: The is_swap of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsIsSwap
        """
        self._is_swap = is_swap

    @property
    def sample_interval(self):
        """Gets the sample_interval of this ValueInPropertyVisitors.


        :return: The sample_interval of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsSampleInterval
        """
        return self._sample_interval

    @sample_interval.setter
    def sample_interval(self, sample_interval):
        """Sets the sample_interval of this ValueInPropertyVisitors.


        :param sample_interval: The sample_interval of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsSampleInterval
        """
        self._sample_interval = sample_interval

    @property
    def data_min(self):
        """Gets the data_min of this ValueInPropertyVisitors.


        :return: The data_min of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsDataMin
        """
        return self._data_min

    @data_min.setter
    def data_min(self, data_min):
        """Sets the data_min of this ValueInPropertyVisitors.


        :param data_min: The data_min of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsDataMin
        """
        self._data_min = data_min

    @property
    def data_max(self):
        """Gets the data_max of this ValueInPropertyVisitors.


        :return: The data_max of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsDataMax
        """
        return self._data_max

    @data_max.setter
    def data_max(self, data_max):
        """Sets the data_max of this ValueInPropertyVisitors.


        :param data_max: The data_max of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsDataMax
        """
        self._data_max = data_max

    @property
    def node_id(self):
        """Gets the node_id of this ValueInPropertyVisitors.


        :return: The node_id of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsNodeId
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ValueInPropertyVisitors.


        :param node_id: The node_id of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsNodeId
        """
        self._node_id = node_id

    @property
    def browse_name(self):
        """Gets the browse_name of this ValueInPropertyVisitors.


        :return: The browse_name of this ValueInPropertyVisitors.
        :rtype: ValueInPropertyVisitorsBrowseName
        """
        return self._browse_name

    @browse_name.setter
    def browse_name(self, browse_name):
        """Sets the browse_name of this ValueInPropertyVisitors.


        :param browse_name: The browse_name of this ValueInPropertyVisitors.
        :type: ValueInPropertyVisitorsBrowseName
        """
        self._browse_name = browse_name

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
        if not isinstance(other, ValueInPropertyVisitors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
