# coding: utf-8

import pprint
import re

import six





class ListReposDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'name': 'str',
        'category': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'name': 'name',
        'category': 'category',
        'filter': 'filter'
    }

    def __init__(self, namespace=None, name=None, category=None, filter=None):
        """ListReposDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._name = None
        self._category = None
        self._filter = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if filter is not None:
            self.filter = filter

    @property
    def namespace(self):
        """Gets the namespace of this ListReposDetailsRequest.

        组织名称

        :return: The namespace of this ListReposDetailsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListReposDetailsRequest.

        组织名称

        :param namespace: The namespace of this ListReposDetailsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def name(self):
        """Gets the name of this ListReposDetailsRequest.

        镜像仓库名称

        :return: The name of this ListReposDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListReposDetailsRequest.

        镜像仓库名称

        :param name: The name of this ListReposDetailsRequest.
        :type: str
        """
        self._name = name

    @property
    def category(self):
        """Gets the category of this ListReposDetailsRequest.

        镜像仓库分类，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :return: The category of this ListReposDetailsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListReposDetailsRequest.

        镜像仓库分类，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :param category: The category of this ListReposDetailsRequest.
        :type: str
        """
        self._category = category

    @property
    def filter(self):
        """Gets the filter of this ListReposDetailsRequest.

        应填写 center::{center}|limit::{limit}|offset::{offset}|order_column::{order_column}|order_type::{order_type} , 其中{center}为self或thirdparty，自己的镜像或第三方镜像，默认值为self,{limit}为返回条数,{offset}为起始索引, {order_column}为按列排序，可设置为name、updated_time、tag_count,{order_type}为排序类型，可设置为desc（降序）、asc（升序）

        :return: The filter of this ListReposDetailsRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListReposDetailsRequest.

        应填写 center::{center}|limit::{limit}|offset::{offset}|order_column::{order_column}|order_type::{order_type} , 其中{center}为self或thirdparty，自己的镜像或第三方镜像，默认值为self,{limit}为返回条数,{offset}为起始索引, {order_column}为按列排序，可设置为name、updated_time、tag_count,{order_type}为排序类型，可设置为desc（降序）、asc（升序）

        :param filter: The filter of this ListReposDetailsRequest.
        :type: str
        """
        self._filter = filter

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
        if not isinstance(other, ListReposDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
