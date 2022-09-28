# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNotebookResponse(SdkResponse):

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
        'description': 'str',
        'creator': 'str',
        'url': 'str',
        'flavor': 'FlavorInfo',
        'status': 'NotebookStatus',
        'image': 'NotebookImage',
        'storages': 'list[NotebookStorage]',
        'create_time': 'str',
        'update_time': 'str',
        'failed_message': 'str',
        'events': 'list[TaskEventRsp]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'creator': 'creator',
        'url': 'url',
        'flavor': 'flavor',
        'status': 'status',
        'image': 'image',
        'storages': 'storages',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'failed_message': 'failed_message',
        'events': 'events'
    }

    def __init__(self, id=None, name=None, description=None, creator=None, url=None, flavor=None, status=None, image=None, storages=None, create_time=None, update_time=None, failed_message=None, events=None):
        """ShowNotebookResponse

        The model defined in huaweicloud sdk

        :param id: notebook ID
        :type id: str
        :param name: notebook名称
        :type name: str
        :param description: notebook描述
        :type description: str
        :param creator: notebook所属用户
        :type creator: str
        :param url: notebook访问URL
        :type url: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkeihealth.v1.FlavorInfo`
        :param status: 
        :type status: :class:`huaweicloudsdkeihealth.v1.NotebookStatus`
        :param image: 
        :type image: :class:`huaweicloudsdkeihealth.v1.NotebookImage`
        :param storages: notebook存储信息
        :type storages: list[:class:`huaweicloudsdkeihealth.v1.NotebookStorage`]
        :param create_time: notebook创建时间
        :type create_time: str
        :param update_time: notebook更新时间
        :type update_time: str
        :param failed_message: notebook失败信息
        :type failed_message: str
        :param events: cce事件
        :type events: list[:class:`huaweicloudsdkeihealth.v1.TaskEventRsp`]
        """
        
        super(ShowNotebookResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._creator = None
        self._url = None
        self._flavor = None
        self._status = None
        self._image = None
        self._storages = None
        self._create_time = None
        self._update_time = None
        self._failed_message = None
        self._events = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if creator is not None:
            self.creator = creator
        if url is not None:
            self.url = url
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if image is not None:
            self.image = image
        if storages is not None:
            self.storages = storages
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if failed_message is not None:
            self.failed_message = failed_message
        if events is not None:
            self.events = events

    @property
    def id(self):
        """Gets the id of this ShowNotebookResponse.

        notebook ID

        :return: The id of this ShowNotebookResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowNotebookResponse.

        notebook ID

        :param id: The id of this ShowNotebookResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowNotebookResponse.

        notebook名称

        :return: The name of this ShowNotebookResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowNotebookResponse.

        notebook名称

        :param name: The name of this ShowNotebookResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowNotebookResponse.

        notebook描述

        :return: The description of this ShowNotebookResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowNotebookResponse.

        notebook描述

        :param description: The description of this ShowNotebookResponse.
        :type description: str
        """
        self._description = description

    @property
    def creator(self):
        """Gets the creator of this ShowNotebookResponse.

        notebook所属用户

        :return: The creator of this ShowNotebookResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ShowNotebookResponse.

        notebook所属用户

        :param creator: The creator of this ShowNotebookResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def url(self):
        """Gets the url of this ShowNotebookResponse.

        notebook访问URL

        :return: The url of this ShowNotebookResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowNotebookResponse.

        notebook访问URL

        :param url: The url of this ShowNotebookResponse.
        :type url: str
        """
        self._url = url

    @property
    def flavor(self):
        """Gets the flavor of this ShowNotebookResponse.


        :return: The flavor of this ShowNotebookResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FlavorInfo`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ShowNotebookResponse.


        :param flavor: The flavor of this ShowNotebookResponse.
        :type flavor: :class:`huaweicloudsdkeihealth.v1.FlavorInfo`
        """
        self._flavor = flavor

    @property
    def status(self):
        """Gets the status of this ShowNotebookResponse.


        :return: The status of this ShowNotebookResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NotebookStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowNotebookResponse.


        :param status: The status of this ShowNotebookResponse.
        :type status: :class:`huaweicloudsdkeihealth.v1.NotebookStatus`
        """
        self._status = status

    @property
    def image(self):
        """Gets the image of this ShowNotebookResponse.


        :return: The image of this ShowNotebookResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NotebookImage`
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ShowNotebookResponse.


        :param image: The image of this ShowNotebookResponse.
        :type image: :class:`huaweicloudsdkeihealth.v1.NotebookImage`
        """
        self._image = image

    @property
    def storages(self):
        """Gets the storages of this ShowNotebookResponse.

        notebook存储信息

        :return: The storages of this ShowNotebookResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NotebookStorage`]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        """Sets the storages of this ShowNotebookResponse.

        notebook存储信息

        :param storages: The storages of this ShowNotebookResponse.
        :type storages: list[:class:`huaweicloudsdkeihealth.v1.NotebookStorage`]
        """
        self._storages = storages

    @property
    def create_time(self):
        """Gets the create_time of this ShowNotebookResponse.

        notebook创建时间

        :return: The create_time of this ShowNotebookResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowNotebookResponse.

        notebook创建时间

        :param create_time: The create_time of this ShowNotebookResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowNotebookResponse.

        notebook更新时间

        :return: The update_time of this ShowNotebookResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowNotebookResponse.

        notebook更新时间

        :param update_time: The update_time of this ShowNotebookResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def failed_message(self):
        """Gets the failed_message of this ShowNotebookResponse.

        notebook失败信息

        :return: The failed_message of this ShowNotebookResponse.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        """Sets the failed_message of this ShowNotebookResponse.

        notebook失败信息

        :param failed_message: The failed_message of this ShowNotebookResponse.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def events(self):
        """Gets the events of this ShowNotebookResponse.

        cce事件

        :return: The events of this ShowNotebookResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskEventRsp`]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ShowNotebookResponse.

        cce事件

        :param events: The events of this ShowNotebookResponse.
        :type events: list[:class:`huaweicloudsdkeihealth.v1.TaskEventRsp`]
        """
        self._events = events

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
        if not isinstance(other, ShowNotebookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
