# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'namspace_num': 'int',
        'repo_num': 'int',
        'image_num': 'int',
        'store_space': 'float',
        'downflow_size': 'float'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'namspace_num': 'namspace_num',
        'repo_num': 'repo_num',
        'image_num': 'image_num',
        'store_space': 'store_space',
        'downflow_size': 'downflow_size'
    }

    def __init__(self, domain_id=None, domain_name=None, namspace_num=None, repo_num=None, image_num=None, store_space=None, downflow_size=None):
        r"""ShowDomainOverviewResponse

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param domain_name: 租户名称
        :type domain_name: str
        :param namspace_num: 当前租户的命名空间个数
        :type namspace_num: int
        :param repo_num: 当前租户的仓库个数
        :type repo_num: int
        :param image_num: 当前租户的镜像个数
        :type image_num: int
        :param store_space: 当前租户存储大小
        :type store_space: float
        :param downflow_size: 当前租户下载流量大小
        :type downflow_size: float
        """
        
        super(ShowDomainOverviewResponse, self).__init__()

        self._domain_id = None
        self._domain_name = None
        self._namspace_num = None
        self._repo_num = None
        self._image_num = None
        self._store_space = None
        self._downflow_size = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if namspace_num is not None:
            self.namspace_num = namspace_num
        if repo_num is not None:
            self.repo_num = repo_num
        if image_num is not None:
            self.image_num = image_num
        if store_space is not None:
            self.store_space = store_space
        if downflow_size is not None:
            self.downflow_size = downflow_size

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowDomainOverviewResponse.

        租户ID

        :return: The domain_id of this ShowDomainOverviewResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowDomainOverviewResponse.

        租户ID

        :param domain_id: The domain_id of this ShowDomainOverviewResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainOverviewResponse.

        租户名称

        :return: The domain_name of this ShowDomainOverviewResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainOverviewResponse.

        租户名称

        :param domain_name: The domain_name of this ShowDomainOverviewResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def namspace_num(self):
        r"""Gets the namspace_num of this ShowDomainOverviewResponse.

        当前租户的命名空间个数

        :return: The namspace_num of this ShowDomainOverviewResponse.
        :rtype: int
        """
        return self._namspace_num

    @namspace_num.setter
    def namspace_num(self, namspace_num):
        r"""Sets the namspace_num of this ShowDomainOverviewResponse.

        当前租户的命名空间个数

        :param namspace_num: The namspace_num of this ShowDomainOverviewResponse.
        :type namspace_num: int
        """
        self._namspace_num = namspace_num

    @property
    def repo_num(self):
        r"""Gets the repo_num of this ShowDomainOverviewResponse.

        当前租户的仓库个数

        :return: The repo_num of this ShowDomainOverviewResponse.
        :rtype: int
        """
        return self._repo_num

    @repo_num.setter
    def repo_num(self, repo_num):
        r"""Sets the repo_num of this ShowDomainOverviewResponse.

        当前租户的仓库个数

        :param repo_num: The repo_num of this ShowDomainOverviewResponse.
        :type repo_num: int
        """
        self._repo_num = repo_num

    @property
    def image_num(self):
        r"""Gets the image_num of this ShowDomainOverviewResponse.

        当前租户的镜像个数

        :return: The image_num of this ShowDomainOverviewResponse.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this ShowDomainOverviewResponse.

        当前租户的镜像个数

        :param image_num: The image_num of this ShowDomainOverviewResponse.
        :type image_num: int
        """
        self._image_num = image_num

    @property
    def store_space(self):
        r"""Gets the store_space of this ShowDomainOverviewResponse.

        当前租户存储大小

        :return: The store_space of this ShowDomainOverviewResponse.
        :rtype: float
        """
        return self._store_space

    @store_space.setter
    def store_space(self, store_space):
        r"""Sets the store_space of this ShowDomainOverviewResponse.

        当前租户存储大小

        :param store_space: The store_space of this ShowDomainOverviewResponse.
        :type store_space: float
        """
        self._store_space = store_space

    @property
    def downflow_size(self):
        r"""Gets the downflow_size of this ShowDomainOverviewResponse.

        当前租户下载流量大小

        :return: The downflow_size of this ShowDomainOverviewResponse.
        :rtype: float
        """
        return self._downflow_size

    @downflow_size.setter
    def downflow_size(self, downflow_size):
        r"""Sets the downflow_size of this ShowDomainOverviewResponse.

        当前租户下载流量大小

        :param downflow_size: The downflow_size of this ShowDomainOverviewResponse.
        :type downflow_size: float
        """
        self._downflow_size = downflow_size

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
        if not isinstance(other, ShowDomainOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
