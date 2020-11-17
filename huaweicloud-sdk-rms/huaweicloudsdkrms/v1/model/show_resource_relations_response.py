# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowResourceRelationsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'relations': 'list[ResourceRelation]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'relations': 'relations',
        'page_info': 'page_info'
    }

    def __init__(self, relations=None, page_info=None):
        """ShowResourceRelationsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._relations = None
        self._page_info = None
        self.discriminator = None

        if relations is not None:
            self.relations = relations
        if page_info is not None:
            self.page_info = page_info

    @property
    def relations(self):
        """Gets the relations of this ShowResourceRelationsResponse.

        资源关系列表

        :return: The relations of this ShowResourceRelationsResponse.
        :rtype: list[ResourceRelation]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this ShowResourceRelationsResponse.

        资源关系列表

        :param relations: The relations of this ShowResourceRelationsResponse.
        :type: list[ResourceRelation]
        """
        self._relations = relations

    @property
    def page_info(self):
        """Gets the page_info of this ShowResourceRelationsResponse.


        :return: The page_info of this ShowResourceRelationsResponse.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ShowResourceRelationsResponse.


        :param page_info: The page_info of this ShowResourceRelationsResponse.
        :type: PageInfo
        """
        self._page_info = page_info

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
        if not isinstance(other, ShowResourceRelationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
