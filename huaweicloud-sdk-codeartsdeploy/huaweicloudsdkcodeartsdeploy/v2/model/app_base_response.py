# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppBaseResponse:

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
        'region': 'str',
        'arrange_infos': 'list[TaskBaseBody]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'arrange_infos': 'arrange_infos'
    }

    def __init__(self, id=None, name=None, region=None, arrange_infos=None):
        r"""AppBaseResponse

        The model defined in huaweicloud sdk

        :param id: 创建的应用id
        :type id: str
        :param name: 创建应用名称
        :type name: str
        :param region: 应用所属区域
        :type region: str
        :param arrange_infos: 部署任务列表信息
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskBaseBody`]
        """
        
        

        self._id = None
        self._name = None
        self._region = None
        self._arrange_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        if arrange_infos is not None:
            self.arrange_infos = arrange_infos

    @property
    def id(self):
        r"""Gets the id of this AppBaseResponse.

        创建的应用id

        :return: The id of this AppBaseResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AppBaseResponse.

        创建的应用id

        :param id: The id of this AppBaseResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AppBaseResponse.

        创建应用名称

        :return: The name of this AppBaseResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AppBaseResponse.

        创建应用名称

        :param name: The name of this AppBaseResponse.
        :type name: str
        """
        self._name = name

    @property
    def region(self):
        r"""Gets the region of this AppBaseResponse.

        应用所属区域

        :return: The region of this AppBaseResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AppBaseResponse.

        应用所属区域

        :param region: The region of this AppBaseResponse.
        :type region: str
        """
        self._region = region

    @property
    def arrange_infos(self):
        r"""Gets the arrange_infos of this AppBaseResponse.

        部署任务列表信息

        :return: The arrange_infos of this AppBaseResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskBaseBody`]
        """
        return self._arrange_infos

    @arrange_infos.setter
    def arrange_infos(self, arrange_infos):
        r"""Sets the arrange_infos of this AppBaseResponse.

        部署任务列表信息

        :param arrange_infos: The arrange_infos of this AppBaseResponse.
        :type arrange_infos: list[:class:`huaweicloudsdkcodeartsdeploy.v2.TaskBaseBody`]
        """
        self._arrange_infos = arrange_infos

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
        if not isinstance(other, AppBaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
