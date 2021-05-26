# coding: utf-8

import pprint
import re

import six





class ListDeviceGroupsRequest:


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
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'last_modified_time': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'last_modified_time': 'last_modified_time',
        'app_id': 'app_id'
    }

    def __init__(self, instance_id=None, limit=None, marker=None, offset=None, last_modified_time=None, app_id=None):
        """ListDeviceGroupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._last_modified_time = None
        self._app_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if app_id is not None:
            self.app_id = app_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDeviceGroupsRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDeviceGroupsRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this ListDeviceGroupsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListDeviceGroupsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为1-50的整数。

        :return: The limit of this ListDeviceGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDeviceGroupsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为1-50的整数。

        :param limit: The limit of this ListDeviceGroupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListDeviceGroupsRequest.

        上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 

        :return: The marker of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDeviceGroupsRequest.

        上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 

        :param marker: The marker of this ListDeviceGroupsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListDeviceGroupsRequest.

        表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。

        :return: The offset of this ListDeviceGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDeviceGroupsRequest.

        表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。

        :param offset: The offset of this ListDeviceGroupsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ListDeviceGroupsRequest.

        查询设备组在last_modified_time之后修改的记录，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The last_modified_time of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ListDeviceGroupsRequest.

        查询设备组在last_modified_time之后修改的记录，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param last_modified_time: The last_modified_time of this ListDeviceGroupsRequest.
        :type: str
        """
        self._last_modified_time = last_modified_time

    @property
    def app_id(self):
        """Gets the app_id of this ListDeviceGroupsRequest.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的设备组列表，不携带该参数则会查询该用户下所有设备组列表。

        :return: The app_id of this ListDeviceGroupsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListDeviceGroupsRequest.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的设备组列表，不携带该参数则会查询该用户下所有设备组列表。

        :param app_id: The app_id of this ListDeviceGroupsRequest.
        :type: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ListDeviceGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
